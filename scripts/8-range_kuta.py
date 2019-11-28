from method import *
from math import *


def range_kuta(f, xi, yi, xf, order=4, h=0.1):
    def calculate_delta_yn(xn, yn, delta_xn):
        if order == 4:
            delta_1 = f(xn, yn) * delta_xn
            delta_2 = f(xn + delta_xn / 2, yn + delta_1 / 2) * delta_xn
            delta_3 = f(xn + delta_xn / 2, yn + delta_2 / 2) * delta_xn
            delta_4 = f(xn + delta_xn, yn + delta_3) * delta_xn
            return delta_1 / 6 + delta_2 / 3 + delta_3 / 3 + delta_4 / 6
        elif order == 2:
            return f(xn + delta_xn / 2, yn + delta_xn / 2 * f(xn, yn)) * delta_xn
        else:
            raise Exception("Invalid order for Range-Kuta method")

    def iterate(xn, yn, end, delta_xn):
        while xn < end - 0.001:
            delta_yn = calculate_delta_yn(xn, yn, delta_xn)
            xn, yn = xn + delta_xn, yn + delta_yn
        return xn, yn

    def calculate_error():
        sl = iterate(xi, yi, xf, h / 2)[1]
        sll = iterate(xi, yi, xf, h / 4)[1]
        absolute_error = (sll - sl) / (2 ** order - 1)
        return absolute_error / sll

    def calculate_qc():
        s = iterate(xi, yi, xf, h)[1]
        sl = iterate(xi, yi, xf, h / 2)[1]
        sll = iterate(xi, yi, xf, h / 4)[1]
        return (sl - s) / (sll - sl)

    print(calculate_qc())

    return iterate(xi, yi, xf, h)

for xf in range(1, 100):
    met = RangeKuta(lambda x, y: sin(x), 0, 0, xf / 10)
    print(met.get_guess())