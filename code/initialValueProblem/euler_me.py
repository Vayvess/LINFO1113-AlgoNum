import numpy as np


# Not complete
def euler_me(f, a, b, y_init, h):
    def dfn(g, px, n, eps=1e-2, memo={}):
        if px in memo:
            return memo[px]
        if n == 1:
            return (g(px + eps) - g(px - eps)) / (2 * eps)
        a = dfn(g, px + eps, n - 1, eps, memo)
        memo[px + eps] = a
        b = dfn(g, px - eps, n - 1, eps, memo)
        memo[px - eps] = b
        return (a - b) / (2 * eps)

    vx, vy, = np.arange(a, b + h, h), [y_init]
    for x in vx:
        y_init = y_init + h * np.array([dfn(f, x, i) for i in range(1, len(y_init))])
        vy.append(y_init)
    return vx, np.array(vy)


def func(x):
    return x ** 3


a_interval = 0.0
b_interval = 2.0
y_initial = np.array([0.0, 1.0])
h_step = 0.05


X, Y = euler_me(func, a_interval, b_interval, y_initial, h_step)
yExact = X ** 3


print(f'X : {X}')
print(f'Y : {Y}')
print('my version')
