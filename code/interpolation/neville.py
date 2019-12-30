import numpy as np
from time import time


def benchmark(f):
    def wrapper(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        return f'{f.__name__} has taken {time() - start} runtime secs'
    return wrapper


@benchmark
def me(vx, vy, x):
    def worker(i, j):
        if i == j:
            return vy[i]
        a = (x - vx[j]) * worker(i, j - 1)
        b = (vx[i] - x) * worker(i + 1, j)
        return (a + b) / (vx[i] - vx[j])
    return worker(0, len(vx) - 1)


@benchmark
def better_me(vx, vy, x):
    def worker(i, j):
        if i == j:
            return vy[i]
        return ((x - vx[j]) * worker(i, j - 1) + (vx[i] - x) * worker(i + 1, j)) / (vx[i] - vx[j])
    return worker(0, len(vx) - 1)


@benchmark
def felix(xData, yData, x):
    def neville_(xData, yData, x):
        if len(xData) == 1:
            return yData[0]
        else:
            num1 = (x - xData[-1]) * neville_(xData[:-1], yData[:-1], x)
            num2 = (xData[0] - x) * neville_(xData[1:], yData[1:], x)
            den = xData[0] - xData[-1]
            return (num1+num2)/den
    return neville_(xData, yData, x)


@benchmark
def iterative(xData, yData, x):
    m = len(xData)
    y = yData.copy()
    for k in range(1, m):
        y[0:m-k] = ((x - xData[k:m])*y[0:m-k] + (xData[0:m-k] - x)*y[1:m-k+1]) / (xData[0:m-k] - xData[k:m])
    return y[0]


test = 1500
x_data = np.arange(0, 20, 1)
y_data = np.arange(0, 40, 2)

print(me(x_data, y_data, test))
print(better_me(x_data, y_data, test))
print(felix(x_data, y_data, test))
print(iterative(x_data, y_data, test))
