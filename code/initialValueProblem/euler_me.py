import numpy as np


# Not complete
def euler_me(f, a, b, y_init, h):
    def vdf(px, n=len(y_init), tol=1e-9):
        if n:
            yield from vdf(px, n - 1)
        return (f(px + tol) - f(px - tol)) / (2 * tol)

    vx, vy, = np.arange(a, b + h, h), [y_init]
    for x in vx:
        y_init = y_init + h * np.array([dfx for dfx in vdf(x)])
        vy.append(y_init)
    return vx, np.array(vy)


a_interval = 0.0
b_interval = 2.0
y_initial = np.array([0.0, 1.0])
h_step = 0.05


X, Y = euler_me(fun, a_interval, b_interval, y_initial, h_step)
yExact = 100.0 * X - 5.0 * X ** 2 + 990.0 * (np.exp(-0.1 * X) - 1.0)

print(f'X : {X}')
print(f'Y : {Y}')
print('my version')
