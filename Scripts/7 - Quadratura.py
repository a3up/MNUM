from math import sin, pi, exp


def integrate(f, inferior, superior, n=4, method=0, tolerance=0.1):
    order = 4 if method else 2

    def trapezoidal(div=n):
        h = (superior - inferior) / div
        ret = f(inferior)
        ret += sum([2 * f(inferior + index * h) for index in range(1, div + 1)])
        ret *= h / 2
        return ret

    def simpson(div=n):
        if n % 2:
            raise ValueError
        h = (superior - inferior) / div
        ret = f(inferior) + f(superior)
        ret += sum([2 * (1 + index % 2) * f(inferior + index * h) for index in range(1, div)])
        ret *= h / 3
        return ret

    implementation = simpson if method else trapezoidal
    while True:
        res = implementation(n)
        break
        res1 = implementation(n * 2)
        res2 = implementation(n * 4)
        if abs(2 ** order - (res1 - res) / (res2 - res1)) > tolerance:
            n *= 2
        else:
            break
    return res


def double_integrate(f, inferior_x, superior_x, inferior_y, superior_y, nx, ny):
    def simpson(div_x, div_y):
        if nx != 2 or ny != 2:
            raise ValueError
        hx = (superior_x - inferior_x) / div_x
        hy = (superior_y - inferior_y) / div_y
        vertices = sum([f(x, y) for x in [inferior_x, superior_x] for y in [inferior_y, superior_y]])
        intermediary = sum([f(inferior_x + hx, y) for y in [inferior_y, superior_y]])
        intermediary += sum([f(x, inferior_y + hy) for x in [inferior_x, superior_x]])
        center = f(inferior_x + hx, inferior_y + hy)
        ret = vertices + 4 * intermediary + 16 * center;
        ret *= (hx * hy) / 9
        return ret

    res = simpson(nx, ny)
    return res


def euler_method(f, x0, xf, y0, h=0.1):
    def implementation(step):
        x, y = x0, y0
        while x <= xf:
            x, y = x + step, y + step * f(x, y)
        return y

    s = implementation(h)
    sl = implementation(h/2)
    sll = implementation(h/4)
    qc = (sl - s) / (sll - sl)
    e = sll - sl

    return s, qc, e


def f2(x):
    if x == 1:
        return 5
    elif x == 2:
        return 6
    elif x == 3:
        return 5.5
    elif x == 4:
        return 7
    elif x == 5:
        return 7.4
    elif x == 6:
        return 8.5
    elif x == 7:
        return 8
    elif x == 8:
        return 6
    elif x == 9:
        return 7
    elif x == 10:
        return 5


if __name__ == '__main__':
    function = lambda x, y: x ** 2 + y ** 2

    print(euler_method(function, 0, 1.4, 0))
