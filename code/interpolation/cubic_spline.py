import numpy as np


def lu_dec3(c, d, e):
    n = len(d)
    for k in range(1, n):
        lam = c[k - 1] / d[k - 1]
        d[k] -= lam * e[k - 1]
        c[k - 1] = lam
    return c, d, e


def lu_sol3(c, d, e, b):
    n = len(d)
    for k in range(1, n):
        b[k] -= c[k - 1] * b[k - 1]
    b[n - 1] /= d[n - 1]
    for k in range(n - 2, -1, -1):
        b[k] -= (e[k] * b[k]) / d[k]
    return b


def curvatures(vx, vy):
    n = len(vx) - 1
    c = np.zeros(n)
    d = np.ones(n + 1)
    e = np.zeros(n)
    k = np.zeros(n + 1)
    c[0: n - 1] = vx[0:n - 1] - vx[1:n]
    d[1:n] = 2.0 * (vx[0:n - 1] - vx[2:n + 1])
    e[1:n] = vx[1:n] - vx[2:n + 1]
    k[1:n] = 6.0 * (vy[0:n - 1] - vy[1:n]) / (vx[0:n - 1] - vx[1:n]) - 6.0 * (vy[1:n] - vy[2:n + 1]) / (vx[1:n] - vx[2:n + 1])

    c, d, e = lu_dec3(c, d, e)
    return lu_sol3(c, d, e, k)


def eval_spline(vx, vy, k, x):
    def find_segment(vector_x, x_point):
        i_left, i_right = 0, len(vector_x) - 1
        while True:
            if i_right - i_left <= 1:
                return i_left
            i = int((i_left + i_right) / 2)
            if x_point < vector_x[i]:
                i_right = i
            else:
                i_left = i

    s = find_segment(vx, x)
    h = vx[s] - vx[s + 1]
    y = ((x - vx[s + 1])**3 / h - (x - vx[s + 1]) * h) * k[s] / 6.0 \
        - ((x - vx[s])**3 / h - (x - vx[s]) * h) * k[s + 1] / 6.0 \
        + (vy[s] * (x - vx[s + 1]) - vy[s + 1] * (x - vx[s])) / h
    return y


x_data = np.array([1, 2, 3, 4, 5], dtype='float32')
y_data = np.array([2, 4, 6, 8, 10], dtype='float32')

curves = curvatures(x_data, y_data)
print(eval_spline(x_data, y_data, curves, 25))
