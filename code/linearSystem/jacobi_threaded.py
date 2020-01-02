# Implementation from Barghest
import numpy as np
from threading import Thread


# Note: Since jacobi's algorithm is iterative
# diminish the tolerance to get stricter results ;)
def jacobi(a, n_threads, tol=0.1e-9):
    """
    :param n_threads: numbers of threads desired to compute the row of x
    :param a: [A/b] -> coefficient matrix of A which last column is the independent term b / A -> SDD matrix
    :param tol: float -> the maximum distance between x and x^-1 such as distance(x, x^-1) < tolerance
    :return: ndarray: the closest vector 'x' of a @ x = b that respect the tolerance
    """

    def distance(curr, old):
        w = curr - old
        return np.dot(w, w).sum()

    n = len(a)
    x, prev = np.zeros(n), np.ones(n)

    def compute(i):
        for i in range(i, n, i + 1):
            sigma = 0
            for j in range(n):
                if i != j:
                    sigma += a[i, j] * x[j]
            x[i] = (1 / a[i, i]) * (a[i, -1] - sigma)

    while distance(x, prev) > tol:
        prev, threads = x.copy(), [Thread(target=compute, args=(i,), daemon=True) for i in range(n_threads)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
    return x


A = np.array([[2, -1, 0, -3],
              [-1, 2, -1, -1],
              [0, -1, 2, 4]], dtype='float')

# Ax = b -> { b = (-3, -1, 4), x = (-1.75, -0.5, 1.75) }
print(jacobi(A, 2))
