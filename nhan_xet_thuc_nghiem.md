# Thực nghiệm so sánh (SV6) – Nhóm 5

**Bài toán:** f(x) = e^(−x²) tại x = 0.5, h = 10⁻¹, 10⁻², …, 10⁻¹².
Giá trị đúng: f'(0.5) = f''(0.5) = −e^(−1/4) ≈ −0.778801.

## 1. Bảng sai số tuyệt đối

| h | Tiến 2đ O(h) | Lùi 2đ O(h) | Tiến 3đ O(h²) | Lùi 3đ O(h²) | Trung tâm O(h²) | f'' trung tâm |
|---|---|---|---|---|---|---|
| 1e−1 | 3.24e−2 | 4.54e−2 | 1.28e−2 | 1.24e−2 | 6.46e−3 | 6.56e−4 |
| 1e−2 | 3.83e−3 | 3.96e−3 | 1.30e−4 | 1.30e−4 | 6.49e−5 | 6.49e−6 |
| 1e−3 | 3.89e−4 | 3.90e−4 | 1.30e−6 | 1.30e−6 | 6.49e−7 | 6.48e−8 |
| 1e−4 | 3.89e−5 | 3.89e−5 | 1.30e−8 | 1.30e−8 | 6.49e−9 | 7.45e−9 |
| 1e−5 | 3.89e−6 | 3.89e−6 | 1.09e−10 | 1.31e−10 | 6.91e−11 | 4.26e−7 |
| 1e−6 | 3.89e−7 | 3.89e−7 | 9.69e−11 | 4.14e−11 | 4.14e−11 | 2.07e−5 |
| 1e−7 | 3.85e−8 | 3.92e−8 | 1.43e−9 | 2.36e−10 | 3.19e−10 | 1.64e−3 |
| 1e−8 | 7.45e−9 | 3.65e−9 | 1.90e−9 | 7.45e−9 | 1.90e−9 | 3.31e−1 |
| 1e−9 | 1.86e−8 | 1.86e−8 | 3.70e−8 | 7.41e−8 | 1.86e−8 | 7.79e−1 |
| 1e−10 | 6.85e−7 | 4.26e−7 | 6.85e−7 | 4.26e−7 | 1.30e−7 | 1.11e+4 |
| 1e−11 | 1.54e−6 | 1.54e−6 | 7.09e−6 | 4.02e−6 | 1.54e−6 | 7.79e−1 |
| 1e−12 | 2.07e−5 | 2.07e−5 | 2.07e−5 | 7.62e−5 | 2.07e−5 | 7.79e−1 |

## 2. Đồ thị
Xem `do_thi_sai_so.png` (thang log–log; trái: f'; phải: f'').

## 3. Nhận xét

**a) Kiểm chứng bậc chính xác (vùng h lớn).** Hệ số góc của đường sai số trên thang log–log, ước lượng cho h từ 10⁻¹ đến 10⁻³:

| Công thức | Hệ số góc | Bậc lý thuyết |
|---|---|---|
| Tiến 2 điểm | 0.96 | 1 |
| Lùi 2 điểm | 1.03 | 1 |
| Tiến 3 điểm | 2.00 | 2 |
| Lùi 3 điểm | 1.99 | 2 |
| Trung tâm | 2.00 | 2 |
| f'' trung tâm | 2.00 | 2 |

Các công thức O(h) có đường dốc 1 (h giảm 10 lần thì sai số giảm khoảng 10 lần); các công thức O(h²) có đường dốc 2 (sai số giảm khoảng 100 lần). Kết quả trùng khớp lý thuyết.

**b) So sánh các công thức.** Ở cùng h, công thức O(h²) chính xác hơn công thức O(h) nhiều bậc (h = 10⁻³: 10⁻⁶ so với 10⁻⁴). Trong nhóm O(h²), sai ph��n trung tâm chính xác nhất (hằng số sai số nhỏ hơn khoảng 2 lần so với tiến/lùi 3 điểm) và chỉ cần 2 lần tính f, nên là lựa chọn tốt khi hàm xác định hai phía. Tiến/lùi 3 điểm dùng ở biên, nơi không có điểm phía ngoài.

**c) Sai số tăng trở lại khi h rất nhỏ.** Tổng sai số ≈ C·h^p (cắt cụt, giảm theo h) + ε·|f|/h (làm tròn, tăng khi h giảm), với ε ≈ 1.1·10⁻¹⁶. Khi h rất nhỏ, f(x+h) và f(x) gần bằng nhau nên phép trừ làm mất chữ số có nghĩa (triệt tiêu), rồi kết quả bị chia cho h rất nhỏ nên sai số làm tròn bị khuếch đại.

| Công thức | h tối ưu (thực nghiệm) | Sai số nhỏ nhất | Dự đoán lý thuyết |
|---|---|---|---|
| Tiến/lùi 2 điểm O(h) | 1e−8 | 7.5e−9 / 3.6e−9 | h ≈ √ε ≈ 1e−8 |
| Trung tâm, tiến/lùi 3 điểm O(h²) | 1e−6 | 4e−11 đến 1e−10 | h ≈ ε^(1/3) ≈ 1e−5…1e−6 |
| f'' trung tâm | 1e−4 | 7.5e−9 | h ≈ ε^(1/4) ≈ 1e−4 |

**d) Đạo hàm cấp 2 nhạy với làm tròn nhất.** Sai số làm tròn của f'' cỡ ε/h² nên h tối ưu lớn hơn (1e−4) và sai số nhỏ nhất (7.5e−9) lớn hơn của đạo hàm cấp 1. Khi h ≤ 1e−8, sai số vọt lên cỡ 0.3 đến 1.1e+4. Tại h = 1e−9, 1e−11, 1e−12 tử số f(x+h) − 2f(x) + f(x−h) bị làm tròn đúng về 0, nên f'' ≈ 0 và sai số bằng chính |f''(0.5)| = 0.779. Điểm 1e−10 (sai số 1.1e+4) là do tử số khác 0 chỉ một bậc làm tròn nhưng chia cho h² = 1e−20.

**e) Kết luận thực hành.** Không nên chọn h càng nhỏ càng tốt. Với số double nên chọn h cỡ 1e−8 cho công thức O(h), cỡ 1e−6 cho O(h²) và cỡ 1e−4 cho đạo hàm cấp 2.
