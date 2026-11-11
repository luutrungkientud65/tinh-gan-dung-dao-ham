# Bài toán ứng dụng (SV7) – Nhóm 5: vận tốc và gia tốc từ số liệu đo

## 1. Mô hình hóa
- Số liệu: 21 điểm, t = 0 → 10 s, bước h = 0.5 s, s làm tròn 0.01 m.
- Mô hình sinh số liệu: s(t) = 100·ln cosh(0.25t), nên
  v(t) = s'(t) = 25·tanh(0.25t), a(t) = v'(t) = 6.25·sech²(0.25t).
- Độ lệch của s làm tròn so với s thật: tối đa 0.0043 m (≤ 0.005 m).

## 2. Phương pháp (dùng các hàm đã cài đặt)
| Đại lượng | Nút trong | Nút biên (t = 0, t = 10) |
|---|---|---|
| Vận tốc v | `diff_table`: sai phân trung tâm O(h²) | `diff_table`: tiến/lùi 3 điểm O(h²) |
| Gia tốc a (cách 1) | `diff2_central` O(h²) | tiến/lùi 4 điểm [2f₀ − 5f₁ + 4f₂ − f₃]/h², O(h²) |
| Gia tốc a (cách 2) | `diff_table` áp dụng lần thứ hai lên dãy v | như trên |

Để tách hai nguồn sai số, mỗi đại lượng được tính lại với s(t) **chưa làm tròn** (chỉ còn sai số cắt cụt).

## 3. Kết quả (xem `ket_qua_ung_dung.csv`, `do_thi_ung_dung.png`)
| Sai số tối đa | s làm tròn 0.01 | s chưa làm tròn |
|---|---|---|
| v (mọi nút) | 0.049 | 0.050 |
| a (nút trong) | 0.047 | 0.015 |
| a (nút biên) | 0.110 | 0.164 |
| a tính từ đạo hàm của v (nút trong) | 0.093 | – |

## 4. Nhận xét: ảnh hưởng của sai số làm tròn
1. **Vận tốc ít bị ảnh hưởng.** Sai số của v gần như không đổi khi bỏ làm tròn (0.049 so với 0.050), nên chủ yếu là sai số cắt cụt của công thức (cỡ h²·s‴/6 với h = 0.5). Phần do làm tròn chỉ tối đa 0.006 m/s (cận lý thuyết ε/h = 0.01). Sai số tương đối của v dưới 0.6% từ t = 0.5 s trở đi.
2. **Gia tốc bị ảnh hưởng mạnh.** Sai số làm tròn của a cỡ 4ε/h² (chia cho h² = 0.25), tối đa 0.08 theo lý thuyết, thực tế đo được 0.042. Với t ≥ 2 s, sai số cắt cụt chỉ còn tối đa 0.0054 nhưng sai số thực tế lên tới 0.047, tức sai số căn quân phương lớn hơn khoảng 5 lần: **sai số làm tròn chiếm ưu thế**. Trên đồ thị, cột sai số của s chưa làm tròn (xám) mượt và nhỏ, còn cột của s làm tròn (đỏ) lên xuống thất thường như nhiễu.
3. **Sai số tương đối của a lớn khi a nhỏ.** Sai số tuyệt đối gần như không đổi theo t trong khi a giảm từ 6.25 xuống 0.17, nên sai số tương đối tăng: 5.9% tại t = 9.5 s, 27.8% tại t = 10 s.
4. **Nút biên kém chính xác hơn.** Công thức một phía có hệ số lớn hơn: v(0) tính được 0.030 (đúng là 0), a(0) lệch 0.110. Ở biên, sai số cắt cụt (0.164 với s chưa làm tròn) còn lớn hơn cả sai số do làm tròn.
5. **Đạo hàm hai lần kém hơn đạo hàm cấp 2 trực tiếp.** Tính a bằng cách đạo hàm dãy v đã tính sai số tối đa 0.093 ở nút trong (xuất hiện tại t = 0.5 s, do sai số của v(0) lan sang), gấp đôi so với `diff2_central` (0.047), vì sai số của v bị đạo hàm tiếp.
6. **Giảm h không giúp.** Sai số làm tròn tăng như 1/h², và h = 0.5 s cố định bởi số liệu đo. Muốn gia tốc đáng tin cậy cần làm trơn dữ liệu (hồi quy bình phương tối thiểu, đa thức bậc thấp trên cửa sổ trượt), tăng độ phân giải của số đo s, hoặc dùng bước lớn hơn (ví dụ h = 1 s) để giảm khuếch đại nhiễu, đổi lại tăng sai số cắt cụt.

## 5. Kết luận
Với số liệu làm tròn 0.01 m và bước 0.5 s, vận tốc tính được đáng tin cậy (sai số < 0.05 m/s), còn gia tốc kém tin cậy hơn nhiều do sai số làm tròn bị khuếch đại 1/h², đặc biệt khi giá trị gia tốc nhỏ và ở các nút biên.
