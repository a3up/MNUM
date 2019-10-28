from math import sqrt, log, exp

inf = float("inf")


def picard_peano(g, guess, i, type = 0):
    dim = len(guess)
    if type == 0:
        for iteration in range(i):
            params = ", ".join([str(x) for x in guess])
            for d in range(dim):
                exec("".join(["guess[d] = g[d](", params, ')']))
    if type == 1:
        for iteration in range(i):
            for d in range(dim):
                params = ", ".join([str(x) for x in guess])
                exec("".join(["guess[d] = g[d](", params, ')']))
    return guess


if __name__ == '__main__':
    system = (lambda x: x - 2 * log(x) - 5,)
    g1 = (lambda x: 2 * log(x) + 5,)
    g2 = (lambda x: exp((x-5)/2),)
    guess1 = [0.01]
    guess2 = [9]
    try:
        print(picard_peano(g1, guess2, 50))
        print(picard_peano(g2, guess1, 50))
    except ValueError:
        print("Value Error")
