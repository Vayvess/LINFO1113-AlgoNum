import numpy as np
from random import randint


def jacobi(a, tol=0.1e-8):
    def distance(curr, old):
        w = curr - old
        return np.dot(w, w).sum()

    n = len(a)
    x, prev = np.zeros(n), np.ones(n)
    while distance(x, prev) > tol:
        prev = x.copy()
        for i in range(n):
            sigma = 0
            for j in range(n):
                if i != j:
                    sigma += a[i, j] * x[j]
            x[i] = (1 / a[i, i]) * (a[i, -1] - sigma)
    return x


size = 10
mx = np.array([[randint(1, 99) for _ in range(size + 1)] for _ in range(size)], dtype='float')
mx = mx @ mx.transpose()
print(jacobi(mx))
