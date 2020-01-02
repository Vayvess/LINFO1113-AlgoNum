import numpy as np
from time import time
from random import randint


def benchmark(f):
    def wrapper(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        return f'{f.__name__} has taken {(time() - start)} runtime in secs'
    return wrapper


def spd_mx(n):
    a = np.array([[randint(1, 99) for _ in range(n)] for _ in range(n)], dtype='float')
    return np.hstack((a @ a.transpose(), np.array([randint(1, 99) for _ in range(n)])[:, None]))
