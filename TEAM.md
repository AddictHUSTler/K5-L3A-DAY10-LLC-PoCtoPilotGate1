# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):
- Lớp: `L3A` / `L3B`
- Repo của bàn: `K5-<L3A|L3B>-DAY10-<TenNhom>-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |           |      |     |             |
|   2 |Trần Thái Hưng| 2A202603557| Kỹ sư cổng |             |
|   3 |           |      |     |             |
|   4 |           |      |     |             |

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

- Câu trong đề: 2.2, 2.6, 3.1, 3.5.
- Mục trong phiếu: Phiếu B mục B2, B7.1; Phiếu C mục C2, C7.
- File: `lab10/guards.py`.
- Chốt cổng vòng 1 bằng `python3 -m lab10.checkpoint`.

### Đóng góp cụ thể

- Dò `T-002@55` và điền bảng soát lỗi ở Phiếu B mục B2, xác định hai lỗi chìm: hoàn sai 20.000đ và ghi lỗi oan cho hãng VNX.
- Soạn HAZOP vòng 1 trên tool `issue_refund` ở Phiếu B mục B4, gồm năm guideword và hai dòng ngoài kỹ thuật.
- Soạn đề xuất pre-mortem bốn lăng kính ở Phiếu B mục B6 để cả bàn thống nhất, gắn với ba cổng: Đúng số tiền, Đúng phê duyệt, Bảo vệ bên thứ ba.
- Dùng AI (Claude Code) để đọc code, soạn nháp B2, B4, B6 và thử nghiệm thiết kế cổng trên bản tạm. Tôi đọc lại và chịu trách nhiệm về nội dung.

### Bằng chứng

- Trace: `python3 -m lab10.trace --suite base --ticket T-002 --seed 55`.
- Phiếu: `templates/form-b-evaluation-gates.md`, mục B2, B4, B6.
- Mã commit:

### Exit ticket

Một điều học được:

Một điều còn chưa chắc:
