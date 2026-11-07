"""
P4 - Dao ham da thuc noi suy Lagrange tai nut.

Cai dat doc lap, khong su dung ham noi suy/dao ham co san.
Tuong thich Python 3.10+.
"""

from math import isfinite
from numbers import Real
from typing import Sequence


def diff_lagrange(xs: Sequence[float], ys: Sequence[float], k: int) -> float:
    """
    Tinh dao ham cua da thuc noi suy Lagrange tai nut xs[k].

    Thuat toan:
        - Tinh he so dao ham cua cac da thuc co so Lagrange tai nut k.
        - Voi i = k: L_k'(x_k) = tong_{j != k} 1 / (x_k - x_j).
        - Voi i != k:
          L_i'(x_k) = [tich_{j != i,k}(x_k - x_j)]
                     / [tich_{j != i}(x_i - x_j)].
        - Tra ve P'(x_k) = tong_i y_i * L_i'(x_k).

    Args:
        xs: Day cac moc noi suy, phai co it nhat 2 gia tri va doi mot.
        ys: Day gia tri ham tai cac moc; ys[i] ung voi xs[i].
        k: Chi so nut can tinh dao ham, bat dau tu 0.

    Returns:
        Gia tri dao ham cua da thuc noi suy tai xs[k] (kieu float).

    Raises:
        TypeError: Neu xs/ys khong phai day so thuc hoac k khong phai so nguyen.
        ValueError: Neu xs va ys khac do dai, co it hon 2 nut, co moc trung
                    nhau, co gia tri khong huu han, hoac k nam ngoai pham vi.

    Notes:
        Cac moc xs khong can cach deu. Do phuc tap tinh toan la O(n^2).
    """
    if isinstance(k, bool) or not isinstance(k, int):
        raise TypeError("k phai la so nguyen.")

    try:
        x_values = list(xs)
        y_values = list(ys)
    except TypeError as exc:
        raise TypeError("xs va ys phai la cac day co the lap.") from exc

    if len(x_values) != len(y_values):
        raise ValueError("xs va ys phai co cung do dai.")

    n = len(x_values)
    if n < 2:
        raise ValueError("Can it nhat 2 nut noi suy de tinh dao ham.")

    if not 0 <= k < n:
        raise ValueError("k nam ngoai pham vi chi so cua xs.")

    for name, values in (("xs", x_values), ("ys", y_values)):
        for value in values:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise TypeError(f"Moi phan tu cua {name} phai la so thuc.")
            if not isfinite(float(value)):
                raise ValueError(f"Moi phan tu cua {name} phai la so huu han.")

    x_values = [float(value) for value in x_values]
    y_values = [float(value) for value in y_values]

    # Kiem tra cac moc noi suy phai phan biet.
    for i in range(n):
        for j in range(i + 1, n):
            if x_values[i] == x_values[j]:
                raise ValueError("Cac moc noi suy xs phai doi mot khac nhau.")

    xk = x_values[k]
    derivative = 0.0

    # Dong gop tu y_k * L_k'(x_k).
    basis_k_derivative = 0.0
    for j in range(n):
        if j != k:
            basis_k_derivative += 1.0 / (xk - x_values[j])
    derivative += y_values[k] * basis_k_derivative

    # Dong gop tu cac y_i * L_i'(x_k), voi i != k.
    for i in range(n):
        if i == k:
            continue

        numerator = 1.0
        for j in range(n):
            if j != i and j != k:
                numerator *= (xk - x_values[j])

        denominator = 1.0
        for j in range(n):
            if j != i:
                denominator *= (x_values[i] - x_values[j])

        derivative += y_values[i] * (numerator / denominator)

    return float(derivative)
