import numpy as np


def euler_book(F, x, y, xStop, h):
    X = []
    Y = []
    X.append(x)
    Y.append(y)
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


x = 0.0
xStop = 2.0
y = np.array([0.0, 1.0])
h = 0.05

X, Y = euler_book(F, x, y, xStop, h)
yExact = 100.0 * X - 5.0 * X ** 2 + 990.0 * (np.exp(-0.1 * X) - 1.0)

print(f'X : {X}')
print(f'Y : {Y}')
print(f'Y_EXACT : {yExact}')
print('book version')
