import math
from random import randint

import numpy as np
import helpers


@helpers.benchmark
def gauss_seidel(a, tol=1.0e-8, lim=69):
    def iter_eqs(curr, omg):
        n = len(curr)
        for i in range(n):
            new = a[i, -1]
            for j in range(n):
                if i != j:
                    new -= a[i, j] * curr[j]
            curr[i] = ((1 - omg) * curr[i]) + ((omg / a[i, i]) * new)
        return curr

    dx1, dx2 = 1, 1
    omega, k, p, x = 1.0, 10, 1, np.zeros(len(a))
    for c in range(lim):
        prev = x.copy()
        x = iter_eqs(x, omega)
        diff = x - prev
        dx = np.sqrt(np.dot(diff, diff))
        # print(f'running iteration {c} dx={dx}')
        if dx < tol:
            return x, c, omega
        if c == k:
            dx1 = dx
        if c == k + p:
            dx2 = dx
            omega = 2.0/(1.0 + math.sqrt(1.0 - math.pow(dx2 / dx1, 1.0 / p)))
    print('gauss-seidel has failed to converge')


A = np.array([[2, -1, 0, -3],
              [-1, 2, -1, -1],
              [0, -1, 2, 4]], dtype='float')


n = 50
mx = np.array([[randint(-25, 25) for _ in range(n)] for _ in range(n)], dtype='float')
mx = mx @ mx.transpose()
b = np.array([[randint(-25, 25)] for _ in range(n)], dtype='float')
mx = np.hstack((mx, b))
print(gauss_seidel(mx))
