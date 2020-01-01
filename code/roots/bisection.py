from time import time
import numpy as np


def benchmark(f):
    def wrapper(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        return f'{f.__name__} has taken {time() - start} runtime secs'
    return wrapper


def root_search(f, a, b, dx=1.e-2):
    x1, f1 = a, f(a)
    x2, f2 = a + dx, f(a + dx)
    while x1 < b:
        if np.sign(f1) != np.sign(f2):
            return x1, x2
        x1, f1 = x2, f2
        x2, f2 = x1 + dx, f(x1 + dx)
    return None, None


def bisection(f, x1, x2, tol=1.e-2):
    while abs(x2 - x1) > tol:
        f1, f2, x3 = f(x1), f(x2), 0.5 * (x1 + x2)
        if np.sign(f1) != np.sign(f(x3)):
            x2 = x3
        else:
            x1 = x3
    return x1, x2


def fun(x):
    return np.power(x, 3) - 10 * np.power(x, 2) + 5


# the last cells of data is the tolerance of bisection / the step made in the root_search
n = 10000
data = (fun, -n, n, 0.5)
bracket = root_search(*data)
print(bracket)
bracket_bi = bisection(fun, -n, n, 1.e-5)
print(bracket_bi)
a, b = bracket_bi
print(fun(a))