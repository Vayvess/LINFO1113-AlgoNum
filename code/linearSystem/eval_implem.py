import numpy as np
from time import time
from random import randint
from threading import Thread


def benchmark(f):
    def wrapper(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        return f'{f.__name__} has taken {(time() - start)} runtime in secs'
    return wrapper


@benchmark
def jacobi_threaded(a, n_threads, tol=0.1e-9):
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


@benchmark
def jacobi(a, tol=0.1e-9):
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


def spd_mx(size):
    a = np.array([[randint(1, 99) for _ in range(size)] for _ in range(size)], dtype='float')
    return np.hstack((a @ a.transpose(), np.array([randint(1, 99) for _ in range(size)])[:, None]))


test = spd_mx(10)
print(jacobi(test))
print(jacobi_threaded(test, 2))
