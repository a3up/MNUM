from math import sin, pi


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
        res1 = implementation(n * 2)
        res2 = implementation(n * 4)
        if abs(2 ** order - (res1 - res)/(res2 - res1)) > tolerance:
            n *= 2
        else:
            break

    return res


if __name__ == '__main__':
    function = lambda x: sin(x) / x ** 2
    divisions = 4
    rounding = 6

    print(round(integrate(function, pi / 2, pi), rounding))
    print(round(integrate(function, pi / 2, pi, method=1), rounding))
