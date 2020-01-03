import numpy as np
from time import time


def benchmark(f):
    def wrapper(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        return f'{f.__name__} has taken {(time() - start)} runtime in secs'
    return wrapper


def fun(x):
    return 8 * x**2 - 800 * x


@benchmark
def native_naive(f, vx):
    vy = []
    for i in range(len(vx)):
        y = f(vx[i])
        vy.append(y)
    return np.array(vy)


@benchmark
def native_better(f, vx):
    vy = []
    for x in vx:
        vy.append(f(x))
    return np.array(vy)


@benchmark
def native_comprehension(f, vx):
    return np.array([f(x) for x in vx])


@benchmark
def vectorized(f, vx):
    return np.vectorize(f)(vx)


test = np.arange(0, 100000, 0.1)
print(native_naive(fun, test))
print(native_better(fun, test))
print(native_comprehension(fun, test))
print(vectorized(fun, test))
