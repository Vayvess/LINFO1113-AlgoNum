import numpy as np
import matplotlib.pyplot as plt


def ridder(f, x0, x2, tol=1.0e-9):
    while abs(f(x2)) > tol:
        x1 = (x0 + x2) * 0.5
        fx0, fx1, fx2 = f(x0), f(x1), f(x2)
        x3 = x1 + (x1 - x0) * (np.sign(fx0) * fx1) / np.sqrt(np.power(fx1, 2) - fx0 * fx2)

        if np.sign(x1) != np.sign(x3):
            x0, x2 = x1, x3
        else:
            x0, x2 = x2 if np.sign(x2) != np.sign(x3) else x0, x3
    return x2


def fun(x):
    return np.power(x, 2) - 9


def plot_me(f, n, root):
    vx = np.arange(-n, n + 1, 1)
    vy = np.array([f(x) for x in vx])
    plt.plot(vx, vy, root, f(root), 'o')
    plt.grid(True)
    plt.show()


test = ridder(fun, 0, 50, 1e-9)
print(test)
plot_me(fun, 10, test)
