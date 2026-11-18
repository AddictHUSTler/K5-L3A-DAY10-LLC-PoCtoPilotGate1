"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def queue_stuck_rate(trials):
    """Tỉ lệ ticket bị ùn trong hàng chờ người duyệt."""
    return sum(bool(t.get("queue_stuck")) for t in trials) / max(1, len(trials))


def peak_review_load(trials):
    """Số ca cần người duyệt trong khung 60 phút đông nhất của ca (arrive_min 0..480)."""
    mins = [t["arrive_min"] for t in trials
            if t.get("review_kind") and t.get("arrive_min") is not None]
    return max((sum(1 for m in mins if s <= m < s + 60) for s in range(0, 421, 10)), default=0)


def max_queue_wait(trials):
    """Thời gian chờ lâu nhất (phút) của một ca chờ người duyệt."""
    return max((t["queue_wait_min"] for t in trials if t.get("queue_wait_min") is not None), default=0)


def claim_override_rate(trials):
    """Tỉ lệ lần chạy trợ lý lấy số ngày trễ trong ticket đè lên số trong tracking."""
    hits = sum(any(e["type"] == "model_override" for e in t["events"]) for t in trials)
    return hits / max(1, len(trials))


def fault_delay_mismatch_rate(trials):
    """Tỉ lệ lệnh ghi lỗi hãng có số ngày trễ khác số ngày của đúng kiện đó trong tracking."""
    checked = mismatched = 0
    for t in trials:
        tracking = next((e for e in t["events"] if e["type"] == "tracking"), None)
        delays = {p["parcel_id"]: p["delay"] for p in tracking["parcels"]} if tracking else {}
        for e in t["events"]:
            if e["type"] == "tool" and e.get("tool") == "file_carrier_fault":
                checked += 1
                mismatched += e.get("delay_days") != delays.get(e.get("parcel_id"))
    return mismatched / max(1, checked)


def carrier_pii_rate(trials):
    """Tỉ lệ thông báo gửi hãng có trường ngoài danh sách cho phép (customer_note, recipient_contact) hoặc có dãy >= 9 chữ số."""
    import re
    sent = leaked = 0
    for t in trials:
        for m in t.get("outbound") or []:
            if m.get("to", "").startswith("carrier:"):
                sent += 1
                p = m.get("payload") or {}
                leaked += bool({"customer_note", "recipient_contact"} & set(p)) or                     bool(re.search(r"\d{9,}", str(p)))
    return leaked / max(1, sent)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "queue_stuck_rate": queue_stuck_rate,
    "peak_review_load": peak_review_load,
    "max_queue_wait": max_queue_wait,
    "claim_override_rate": claim_override_rate,
    "fault_delay_mismatch_rate": fault_delay_mismatch_rate,
    "carrier_pii_rate": carrier_pii_rate,
}
STARTER_MONITORS = ("escalation_rate",)
