# By Barghest a.k.a Raphaël Wats
import math


def dfn(g, x, n, h=1e-2, memo={}):
    if x in memo:
        return memo[x]
    if n == 1:
        return (g(x + h) - g(x - h)) / (2 * h)
    a = dfn(g, x + h, n - 1, h, memo)
    memo[x + h] = a
    b = dfn(g, x - h, n - 1, h, memo)
    memo[x - h] = b
    return (a - b) / (2 * h)


def polynomial_evaluation(coefficients, x):
    sigma = 0
    for i, c in enumerate(coefficients):
        sigma += c * math.pow(x, i)
    return sigma


def derives_polynomial_n_times(n, c):
    return derives_polynomial_n_times(n - 1, [c[i] * i for i in range(1, len(c))]) if n else c


def func(x):
    return 2 + (3 * x) + (7 * x ** 2) + (11 * x ** 3)


if __name__ == '__main__':
    n_times = 2

    # y = 2 + 3x + 7x² + 11x³
    y_coefficients = [2, 3, 7, 11]

    # y" = 14 + 66x
    y_n_derivative_coefficients = derives_polynomial_n_times(n_times, y_coefficients)
    print(y_n_derivative_coefficients)

    # Evaluation
    px = 2
    print(polynomial_evaluation(y_n_derivative_coefficients, px))
    print(dfn(func, px, n_times))
