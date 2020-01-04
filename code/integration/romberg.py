import numpy as np
from trapezoid import *


def romberg(f, a, b, tol=1.0e-6):
    def richardson(richard, m):
        for j in range(m - 1, 0, -1):
            const = 4.0**(m - j)
            richard[j] = (const * richard[j + 1] - richard[j]) / (const - 1.0)
        return richard

    r = np.zeros(21)
    r[1] = trapezoid(f, a, b, 0.0, 1)
    r_old = r[1]
    for k in range(2, 21):
        r[k] = trapezoid(f, a, b, r[k-1], k)
        r = richardson(r, k)
        if abs(r[1] - r_old) < tol * max(abs(r[1]), 1.0):
            return r[1], 2**(k-1)
        r_old = r[1]
    print("Romberg quadrature did not converge")


def fun(x):
    return x**2 + 2 * x + 2


def integral_of_fun(x):
    return x**3 / 3 + x**2 + 2 * x


if __name__ == '__main__':
    x1, x2, n_times = 0, 9, 4
    print(romberg(fun, x1, x2))
    ix1, ix2 = integral_of_fun(x1), integral_of_fun(x2)
    print(ix2 - ix1)
