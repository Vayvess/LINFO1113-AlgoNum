import numpy as np
import matplotlib.pyplot as plt


def euler_book(F, x, y, xStop, h):
    X, Y = [x], [y]
    while x < xStop:
        h = min(h, xStop - x)
        y = y + h * F(x, y)
        x = x + h
        X.append(x)
        Y.append(y)
    return np.array(X), np .array(Y)


def F(x, y):
    F = np.zeros(2)
    F[0] = y[1]
    F[1] = -0.1 * y[1] - x
    return F


if __name__ == '__main__':
    x = 0.0
    xStop = 2.0
    y = np.array([0.0, 1.0])
    h = 0.05

    X, Y = euler_book(F, x, y, xStop, h)
    print(X, Y)
    yExact = 100.0 * X - 5.0 * X ** 2 + 990.0 * (np.exp(-0.1 * X) - 1.0)

    # a, a = 0 is a constant as we know f(a) = 0 and f'(a) = 1 ->  y is the numpy array containing those value
    # Y[:, 1] : Y[:, 0] -> [~f(x) for x in X] where f is unknown, Y[:, n] -> [~f'prime at order n'(x) for x in X]
    plt.plot(X, yExact, '-', X, Y[:, 0], 'o')
    plt.grid(True)
    plt.title('slide on IVP example 2')
    plt.show()
