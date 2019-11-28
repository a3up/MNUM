import matplotlib.pyplot as mpl


class Method:
    def __init__(self, f, xi, yi, xf, h):
        self.f = f
        self.xi = xi
        self.yi = yi
        self.xf = xf
        self.h = h

    def get_delta_yn(self, xn, yn):
        return 0

    def iterate(self):
        xn, yn = self.xi, self.yi
        delta_xn = self.h
        while xn < self.xf - 0.001:
            delta_yn = self.get_delta_yn(xn, yn)
            xn, yn = xn + delta_xn, yn + delta_yn
        return xn, yn


class RangeKuta(Method):
    def __init__(self, f, xi, yi, xf, h=0.1, order=4):
        Method.__init__(self, f, xi, yi, xf, h)
        if order != 2 and order != 4:
            raise Exception("Invalid order for Range-Kuta method")
        self.order = order

    def get_delta_yn(self, xn, yn):
        if self.order == 4:
            delta_1 = self.f(xn, yn) * self.h
            delta_2 = self.f(xn + self.h / 2, yn + delta_1 / 2) * self.h
            delta_3 = self.f(xn + self.h / 2, yn + delta_2 / 2) * self.h
            delta_4 = self.f(xn + self.h, yn + delta_3) * self.h
            return delta_1 / 6 + delta_2 / 3 + delta_3 / 3 + delta_4 / 6
        elif self.order == 2:
            return self.f(xn + self.h / 2, yn + self.h / 2 * self.f(xn, yn)) * self.h

    def get_guess(self):
        return self.iterate()

class Graphic:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        xs = [value[0] for value in self.values]
        ys = [value[1] for value in self.values]
        mpl.plot(xs, ys)
        mpl.show()
        return "Graphic plotted"


class Guess:
    def __init__(self, values, absolute_error, relative_error):
        self.values = values
        self.absolute_error = absolute_error
        self.relative_error = relative_error

    def __str__(self):
        return str(self.values[-1])
