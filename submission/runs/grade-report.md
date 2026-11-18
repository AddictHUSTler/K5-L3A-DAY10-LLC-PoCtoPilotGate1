# Tự kiểm tra sự cố S7 · FAIL

*Đây là kết quả TỰ KIỂM TRA của bàn, không phải điểm. Bài được một team chấm tự động chấm lại sau buổi học.*

- Mã lần chạy: `R-S7-grade-20261118-204626-e9beef` · bàn: `K5-L3A-DAY10-LLC-PoCtoPilotGate1` · grader `lab10-1.0` · 0.368s
- Ba mốc: base `R-S7-before-20261118-204626-e9beef` · prepared `R-S7-prepared-20261118-204626-e9beef` · after `R-S7-after-20261118-204626-e9beef` (report + trace trong runs/)
- Mốc prepared (cổng vòng 1): đã chốt `ec9e40b5`, còn nguyên
- Hash code đội (guards + monitors + switches + cổng vận hành): `e9beef1f3709`
- Hash Bản tiêu chí chấp nhận: `f4853f3d36bd` · đã ký: `f4853f3d36bd` · KHÔNG ĐỔI
- Thẻ đang kiểm: `S7` · dòng "Thẻ đã bốc" bàn ghi trong phiếu: S7 · khớp

| Kiểm | Kết quả | Chi tiết |
|---|---|---|
| 1 integrity | ✅ | file khoá bị đổi: không |
| 2 criteria | ✅ | đã ký, còn nguyên |
| 3 visible | ❌ | base có vấn đề: True; after sạch: False; ticket còn hỏng: không; trần còn vượt: ['ROI 0.78 < ngưỡng bàn đặt 1.0'] |
| 4 hidden | — | máy này không có bài kiểm tra ẩn (team chấm sẽ chạy sau buổi học) |
| 5 regression | ✅ | bộ nền pass_rate 0.9909 → 1.0; ca mới hỏng: không |
| 6 monitor | ✅ | metric mới: ['queue_stuck_rate', 'peak_review_load', 'max_queue_wait', 'claim_override_rate', 'fault_delay_mismatch_rate', 'carrier_pii_rate']; sáng đèn: [('peak_review_load', 'before', 15.0, 0.0), ('peak_review_load', 'after', 10.0, 5.0), ('claim_override_rate', 'before', 0.045455, 0.0), ('claim_override_rate', 'after', 0.047059, 0.0), ('fault_delay_mismatch_rate', 'before', 0.017857, 0.0)] |

**Kinh doanh · vận hành · pháp lý trên gói sự cố bàn nhìn thấy** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.0 | 0.1429 | 0.1429 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4405 · 10000 | 5611 · 10000 | 5611 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 682 · 1500 | 782 · 1500 | 782 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 44757 | 30725 | 30725 |
| ROI | 1.27 | 0.78 | 0.78 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 26000 · 2000000 | 25000 · 2000000 | 25000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 0 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.875 | 0.875 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 30 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 0 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 671đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 671đ |
| kho DN | pass 0.0; hoàn sai 0; oan 0; PII 5; chi phí 668đ | — | — |
| kho HCM | pass 0.0; hoàn sai 0; oan 0; PII 15; chi phí 666đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 766đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 766đ |
| kho HN | pass 0.3333; hoàn sai 0; oan 0; PII 10; chi phí 669đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2102đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2102đ |
| hãng DNB | pass 0.0; hoàn sai 0; oan 0; PII 5 | — | — |
| hãng GHSH | pass 0.3333; hoàn sai 0; oan 0; PII 10 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.0; hoàn sai 0; oan 0; PII 15 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Kinh doanh · vận hành · pháp lý trên bộ nền** (tiền tính cho một ngày giả lập)

| Chỉ số | base | prepared | after |
|---|---|---|---|
| tỉ lệ chuyển người duyệt | 0.2273 | 0.2353 | 0.2353 |
| thời gian chờ trung bình (phút) | 0.0 | 0.0 | 0.0 |
| thời gian chờ lâu nhất (phút) | 0.0 | 0.0 | 0.0 |
| số ca bị ùn | 0 | 0 | 0 |
| số người trực · ca duyệt được mỗi giờ | 1 · 6 | 1 · 6 | 1 · 6 |
| nhân viên kiểm lại quyết định tự động (%) | 0 | 10 | 10 |
| chi phí mỗi ticket (đ) · làm tay | 4203 · 10000 | 4400 · 10000 | 4400 · 10000 |
| tiền LLM ticket đắt nhất (đ) · trần | 670 · 1500 | 770 · 1500 | 770 · 1500 |
| tiết kiệm ròng mỗi ngày (đ) | 123542 | 95194 | 95194 |
| ROI | 1.34 | 1.27 | 1.27 |
| tổng hoàn tự động một ngày (đ) · ngân sách | 155000 · 2000000 | 155000 · 2000000 | 155000 · 2000000 |
| tiền hoàn sai ngày tệ nhất (đ) · ngân sách | 20000 · 2000000 | 0 · 2000000 | 0 · 2000000 |
| độ phủ pilot (phần ticket trợ lý xử lý) | 1.0 | 0.7727 | 0.7727 |
| số kho đắt hơn làm tay | 0 | 0 | 0 |
| pháp lý: lần lộ dữ liệu cá nhân cho bên thứ ba | 0 | 0 | 0 |
| pháp lý: lỗi ghi oan cho hãng (bên thứ ba) | 1 | 0 | 0 |

*Theo kho và hãng (cùng chỉ số, tách để đọc phân khúc; tổng không đổi). Điền dòng 'Kho hoặc hãng có số xấu nhất' ở Phiếu B mục B8 / Phiếu C mục C12. Chi tiết: mục `by_segment` trong report.json của từng mốc.*

| Phân khúc | base | prepared | after |
|---|---|---|---|
| kho ? | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 10359đ > làm tay |
| kho CT | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 590đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 665đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 665đ |
| kho DN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 4586đ | — | — |
| kho HCM | pass 0.96; hoàn sai 20000; oan 1; PII 0; chi phí 2571đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3447đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 3447đ |
| kho HN | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 1993đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ | pass 1.0; hoàn sai 0; oan 0; PII 0; chi phí 2079đ |
| hãng ? | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng DNB | pass 1.0; hoàn sai 0; oan 0; PII 0 | — | — |
| hãng GHSH | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng LGX | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng MKD | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |
| hãng VNX | pass 0.9714; hoàn sai 20000; oan 1; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 | pass 1.0; hoàn sai 0; oan 0; PII 0 |

**Trần và ngưỡng ở mốc after (nền của quyết định Gate 1 v2)**

- VƯỢT TRẦN: ROI 0.78 < ngưỡng bàn đặt 1.0 (trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: cost_per_ticket_vnd ≤ 1500 (thực tế 4400, trên base)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: cost_per_ticket_vnd ≤ 1500 (thực tế 5611, trên visible)
- NGƯỠNG ĐÃ KÝ CHƯA ĐẠT: roi ≥ 1.0 (thực tế 0.78, trên visible)
- KHÔNG đủ căn cứ để chọn 'Tiếp tục'. Thu hẹp, Cải tiến thêm hoặc Dừng, kèm lý do và con số, vẫn là quyết định đạt.

| Bộ | Chỉ số | base | prepared | after | Chênh after − base |
|---|---|---|---|---|---|
| base | pass_rate | 0.9909 | 1.0 | 1.0 | +0.0091 |
| base | pass_k | 0.9545 | 1.0 | 1.0 | +0.0455 |
| base | wrongful_refund_vnd | 20000 | 0 | 0 | -20000 |
| base | under_refund_vnd | 0 | 0 | 0 | +0 |
| base | wrongful_carrier_faults | 1 | 0 | 0 | -1 |
| base | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| base | pii_leaks | 0 | 0 | 0 | +0 |
| base | escalation_rate | 0.2273 | 0.1765 | 0.1765 | -0.0508 |
| visible | pass_rate | 0.25 | 1.0 | 1.0 | +0.75 |
| visible | pass_k | 0.25 | 1.0 | 1.0 | +0.75 |
| visible | wrongful_refund_vnd | 0 | 0 | 0 | +0 |
| visible | under_refund_vnd | 0 | 0 | 0 | +0 |
| visible | wrongful_carrier_faults | 0 | 0 | 0 | +0 |
| visible | merchant_debit_vnd | 0 | 0 | 0 | +0 |
| visible | pii_leaks | 30 | 0 | 0 | -30 |
| visible | escalation_rate | 0.0 | 0.0 | 0.0 | +0.0 |
