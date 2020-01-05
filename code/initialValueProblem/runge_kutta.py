import numpy as np
from time import time
import matplotlib.pyplot as plt


def benchmark(f):
    def wrapper(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        return f'{f.__name__} has taken {(time() - start)} runtime in secs'
    return wrapper


def integrate_rk4(F, x, y, xStop, h):
    def run_kut4(F, x, y, h):
        K0 = h * F(x, y)
        K1 = h * F(x + h * 0.5, y + K0 * 0.5)
        K2 = h * F(x + h * 0.5, y + K1 * 0.5)
        K3 = h * F(x + h * 0.5, y + K2)
        return (K0 + 2.0 * K1 + 2.0 * K2 + K3) / 6.0

    X, Y = [x], [y]
    while x < xStop:
        h = min(h, xStop - x)
        y = y + run_kut4(F, x, y, h)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)


def integrate_rk2(F, x, y, xStop, h):
    X, Y = [x], [y]
    while x < xStop:
        h = min(h, xStop - x)
        y = y + h * F(x + h * 0.5, y + h * 0.5 * F(x, y))
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np.array(Y)


def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1 * y[1] - x
    return F


if __name__ == '__main__':
    x = 0.0
    xStop = 5.0
    y = np.array([0.0, 1.0])
    h = 0.5

    X2, Y2 = integrate_rk2(F, x, y, xStop, h)
    X4, Y4 = integrate_rk4(F, x, y, xStop, h)
    yExact = 100.0 * X2 - 5.0 * X2 ** 2 + 990.0 * (np.exp(-0.1 * X2) - 1.0)

    plt.grid(True)

    plt.plot(X2, yExact, '-', X2, Y2[:, 0], 'ro')
    plt.title('Runge-kutta method at order 2 (red dot)')
    plt.show()

    plt.plot(X2, yExact, '-', X4, Y4[:, 0], 'bo')
    plt.title('Runge-kutta method at order 4 (blue dot)')
    plt.show()

    plt.plot(X2, yExact, '-', X2, Y2[:, 0], 'ro', X4, Y4[:, 0], 'bo')
    plt.title('Runge-kutta method at order 2 (red dot) and order 4 (blue dot)')
    plt.show()
    print(benchmark(integrate_rk2(F, x, y, xStop, h)))
    print(benchmark(integrate_rk4(F, x, y, xStop, h)))
