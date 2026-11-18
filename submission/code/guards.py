"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def _policy(ctx):
    """Chính sách có hiệu lực theo ngày, không dựa vào cờ index_active."""
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _approval_valid(ctx, action, amount):
    """Phê duyệt phải đúng ticket, đúng đơn, còn hiệu lực, còn hạn và đủ hạn mức."""
    found = ctx.tools.lookup_approvals(approval_id=action["approval_id"])
    if not found:
        return False
    approval = found[0]
    return (approval["status"] == "valid" and approval["expires_at"] >= ctx.as_of
            and approval["ticket_id"] == action["ticket_id"] and approval["order_id"] == action["order_id"]
            and approval["max_vnd"] >= amount)


def _strikes_of(ctx, carrier_id):
    return len(ctx.tools.fault_rows(carrier_id=carrier_id))


def _auto_refunded_to(ctx, customer_id):
    return sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=customer_id) if not r.get("approval_id"))


def _check_refund(ctx, action):
    """Cổng 1 và 2: số tiền lấy từ tracking, chính sách và sổ cái; phê duyệt phải hợp lệ."""
    order, policy = ctx.tools.lookup_order(action["order_id"]), _policy(ctx)
    if order is None or policy is None:
        return Verdict.escalate("thiếu đơn hàng hoặc chính sách để kiểm tra số tiền")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    refunded = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(order_id=action["order_id"]))
    remaining = max(0, entitled - refunded)
    if remaining == 0:
        return Verdict.deny("không còn khoản được hoàn theo tracking, chính sách và sổ cái")

    amount = min(action["amount_vnd"], remaining)
    limits = ctx.tools.ops_limits()
    if action.get("approval_id"):
        if not _approval_valid(ctx, action, amount):
            return Verdict.escalate("phê duyệt không hợp lệ cho khoản hoàn này")
    else:
        if amount > policy["auto_limit_vnd"]:
            return Verdict.escalate("vượt hạn mức hoàn tự động, chưa có phê duyệt")
        customer_cap = limits.get("max_auto_refund_per_customer_per_day_vnd")
        if customer_cap is not None and _auto_refunded_to(ctx, order["customer_id"]) + amount > customer_cap:
            return Verdict.escalate("vượt trần hoàn tự động cho một khách trong ngày")

    # Tiền được ghi trước lỗi hãng, nên phải kiểm tra trần lỗi của hãng ngay từ bước này.
    strike_cap = limits.get("max_auto_strikes_per_carrier_per_day")
    if strike_cap is not None and H.carrier_at_fault(policy, parcel, delay) \
            and _strikes_of(ctx, parcel["carrier_id"]) >= strike_cap:
        return Verdict.escalate("hãng đã chạm trần lỗi tự động trong ngày, cần người duyệt")

    if amount != action["amount_vnd"] or action.get("payer") != "LOGIX":
        return Verdict.modify("đưa khoản hoàn về đúng số được hưởng", amount_vnd=amount, payer="LOGIX")
    return Verdict.allow()


def _check_fault(ctx, action):
    """Cổng 3: chỉ ghi lỗi đúng kiện, đúng hãng, có căn cứ trong tracking."""
    order, policy = ctx.tools.lookup_order(action["order_id"]), _policy(ctx)
    if order is None or policy is None:
        return Verdict.deny("thiếu đơn hàng hoặc chính sách để ghi lỗi hãng")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)
    if not H.carrier_at_fault(policy, parcel, delay):
        return Verdict.deny("tracking không đủ căn cứ ghi lỗi cho hãng")
    strike_cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
    if strike_cap is not None and _strikes_of(ctx, parcel["carrier_id"]) >= strike_cap:
        return Verdict.deny("hãng đã chạm trần lỗi tự động trong ngày")
    facts = {"parcel_id": parcel["parcel_id"], "carrier_id": parcel["carrier_id"],
             "driver_id": parcel.get("driver_id"), "delay_days": delay}
    if any(action.get(key) != value for key, value in facts.items()):
        return Verdict.modify("ghi lỗi theo đúng kiện và số ngày trong tracking", **facts)
    return Verdict.allow()


def _check_notice(ctx, action):
    """Cổng 3: thông báo cho hãng chỉ chứa các trường chính sách cho phép."""
    policy = _policy(ctx)
    # Chỉ cho đi các trường chính sách cho phép, và không bao giờ cho đi trường pháp lý đã chặn.
    blocked = set(ctx.gates.get("legal", {}).get("pii_fields_blocked_to_third_party", []))
    allowed = (set(policy["carrier_notice_fields"]) if policy else set()) - blocked
    payload = action.get("payload") or {}
    if set(payload) - allowed:
        return Verdict.modify("bỏ các trường không được gửi cho hãng",
                              payload={key: value for key, value in payload.items() if key in allowed})
    return Verdict.allow()


def pre_guard(ctx):
    policy = _policy(ctx)
    if policy is None:
        return Verdict.escalate("không có chính sách đang hiệu lực")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    checks = {"issue_refund": _check_refund, "file_carrier_fault": _check_fault, "notify_carrier": _check_notice}
    check = checks.get(action["tool"])
    return check(ctx, action) if check else Verdict.allow()
