from math import sqrt, log, exp

inf = float("inf")


def gauss(g, guess, error, method=0):
    dim = len(guess)
    n = 0

    def print_actual(n, guess):
        print(end="| ")
        print(" " * (6 - len(str(n))) + str(n), end=" | ")
        for index, value in enumerate(guess):
            value = str(round(value, 3))
            print(" " * (6 - len(value)) + value, end=" | ")
        print()

    def verify_end(old, guess, error):
        finished = True
        for oldValue, newValue in zip(old, guess):
            if abs(oldValue - newValue) > error:
                finished = False
        return finished

    def jordan(g, guess):
        params = ", ".join([str(x) for x in guess])
        for d in range(dim):
            exec("".join(["guess[d] = g[d](", params, ')']))

    def seidel(g, guess):
        for d in range(dim):
            params = ", ".join([str(x) for x in guess])
            exec("".join(["guess[d] = g[d](", params, ')']))

    function = seidel if method else jordan
    while True:
        print_actual(n, guess)
        old = guess.copy()
        function(g, guess)
        if verify_end(old, guess, error):
            break
        n += 1
    return guess


if __name__ == '__main__':
    gs = (lambda x1, x2, x3: (24 - 2 * x2) / 7,
          lambda x1, x2, x3: (27 - 4 * x1 - x3) / 10,
          lambda x1, x2, x3: (27 - 5 * x1 + 2 * x2) / 8)
    guesses = [0, 0, 0]

    print()
    print("+--------+--------+--------+--------+ ")
    print("|      n |     x1 |     x2 |     x3 | ")
    print("+--------+--------+--------+--------+ ")

    res = gauss(gs, guesses, 0.001)

    print("|  Final", end=" | ")
    for i, guess in enumerate(res):
        guess = str(round(guess, 3))
        print(" " * (6 - len(guess)) + guess, end=" | ")

    print()
    print("+--------+--------+--------+--------+ ")
