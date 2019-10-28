inf = float("inf")

def newton(function, derivative, guess, i = 20):
    for i in range(i):
        if abs(guess) == inf:
            return None
        guess = guess - function(guess)/derivative(guess)
    return guess

y = lambda x: 2 * x ** 2 - 5 * x - 2
yl = lambda x: 4 * x - 5

print(newton(y, yl, 5))