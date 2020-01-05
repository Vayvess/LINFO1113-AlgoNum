import numpy as np
import matplotlib.pyplot as plt


# This method is superseded by Ridder's one !
def secant(f, x1, x2, tol=1e-9):
    def compute():
        fx1, fx2 = f(x1), f(x2)
        new = x2 - fx2 * (x2 - x1) / (fx2 - fx1)
        return fx1, fx2, f(new), new

    f1, f2, f3, x3 = compute()
    while f3 > tol:
        x1, x2 = x2, x3
        f1, f2, f3, x3 = compute()
    return x3


def fun(x):
    return np.power(x, 3) - 7 * x + 6


def plot_me(f, px, n):
    vx = np.arange(-n, n + 1, 0.1)
    vy = np.array([f(x) for x in vx])
    plt.plot(vx, vy, '-', px, f(px), 'o')
    plt.grid(True)
    plt.show()


x_point = secant(fun, 1.5, 5)
print(x_point, fun(x_point))
plot_me(fun, x_point, 10)
