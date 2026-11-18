# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên                | MSSV        | Vai                    | Trưởng nhóm |
| --: | ------------------------ | ----------- | ---------------------- | :---------: |
|   1 | Nguyễn Trọng Phương Bách | 2A202603716 | Kỹ sư cổng             |     Có      |
|   2 | Trần Thái Hưng           | 2A202603557 | Kỹ sư cổng             |             |
|   3 | Đỗ Nhật Anh              | 2A202603701 | Sản phẩm và kinh doanh |             |
|   4 |                          |             |                        |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## TranThaiHung-2A202603557

### Phần việc phụ trách

Vai trong bàn: Kỹ sư cổng, phụ trách viết cổng phòng ngừa.

- Câu trong đề: 2.2, 2.6, 2.7, 2.8, 3.1, 3.5.
- Mục trong phiếu: Phiếu B mục B0 (dòng base và after), B2, B3, B5, B7.1, B7.2, B7.3, B7.4, B7.5, B7.6, B8; Phiếu C mục C2, C7.
- File: `lab10/guards.py`, `lab10/monitors.py` (hai chỉ số `claim_override_rate`, `fault_delay_mismatch_rate`), `config/operating_gates.json`.
- Chạy đo chính thức trên máy của mình và chốt cổng vòng 1 bằng `python3 -m lab10.checkpoint`.

### Đóng góp cụ thể

- Dò `T-002@55` và điền bảng soát lỗi ở Phiếu B mục B2, xác định hai lỗi chìm: hoàn sai 20.000đ và ghi lỗi oan cho hãng VNX.
- Soạn HAZOP vòng 1 trên tool `issue_refund` ở Phiếu B mục B4, gồm năm guideword và hai dòng ngoài kỹ thuật.
- Soạn đề xuất pre-mortem bốn lăng kính ở Phiếu B mục B6 để cả bàn thống nhất, gắn với ba cổng: Đúng số tiền, Đúng phê duyệt, Bảo vệ bên thứ ba.
- Viết ba cổng phòng ngừa trong `lab10/guards.py`: Đúng số tiền, Đúng phê duyệt, Bảo vệ bên thứ ba, kèm ghim chính sách theo ngày hiệu lực. Trên bộ nền, `pass_rate` tăng từ 0,9909 lên 1,0, tiền hoàn sai và lỗi ghi oan về 0, không có ca mới hỏng.
- Thêm hai chỉ số theo dõi trong `lab10/monitors.py` để phát hiện trợ lý lấy số ngày trong ticket đè lên tracking và lệnh ghi lỗi hãng lệch số ngày với tracking.
- Đo lại mốc base, đo mốc after và ghi vào Phiếu B mục B0; điền B7.1, B7.2, B7.3 với hai ticket hiểm.
- Điền cổng kinh doanh, vận hành, pháp lý trong `config/operating_gates.json`, checklist B5, runbook B7.5 và giờ cao điểm B7.6, đo lại mốc after với config đầy đủ.
- Điền bản đồ dữ liệu B3, so sánh các phương án phạm vi pilot, đề xuất cắt kho DN và soạn quyết định v1 ở B8.
- Dùng AI (Claude Code) để đọc code, soạn nháp B2, B3, B4, B5, B6, B7.1 đến B7.6, B8, hỗ trợ viết và thử nghiệm cổng, monitor, config. Tôi đọc lại và chịu trách nhiệm về nội dung.

### Bằng chứng

- Trace: `python3 -m lab10.trace --suite base --ticket T-002 --seed 55`.
- Phiếu: `templates/form-b-evaluation-gates.md`, mục B0, B2 đến B6, B7.1 đến B7.6, B8.
- Mã lần chạy: base `R-base-before-20261118-181246-9b453b`, after có cổng `R-base-after-20261118-182903-f36ccc`, after có đủ config `R-base-after-20261118-184907-38d77a`, after sau khi thu hẹp `R-base-after-20261118-185548-5a27af`.
- Mã commit: `0389a67` (B2, B4, B6), `d99dc19` (cổng, monitor, B7.1 đến B7.3).
- Pull Request: #1 (B2, B4, B6), #4 (cổng, monitor, B7.1 đến B7.3).

### Exit ticket

Một điều học được:

Một điều còn chưa chắc:
