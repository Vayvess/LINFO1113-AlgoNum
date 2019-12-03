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


c = np.array([1, 2, 3, 4], np.float32)
d = np.array([1, 2, 3, 4, 5], np.float32)
e = np.array([1, 2, 3, 4], np.float32)

LUc, LUd, LUe = lu_dec3(c, d, e)
b = np.array([1, 2, 3, 4, 5])
result = lu_sol3(LUc, LUd, LUe, b)
print(result)
