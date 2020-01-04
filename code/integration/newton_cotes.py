from time import time


def newton_cotes(f, n, x_start, x_stop):
    h = (x_stop - x_start) / n
    x_current = x_start
    to_r = 0
    for i in range(n):
        to_r += f(x_current) + f(x_current + h)
        x_current += h
    return to_r * h / 2


def newton_cotes_better(f, n, a, b):
    h, y = (b - a) / n, (f(a) + f(b)) * 0.5
    for _ in range(n - 1):
        a += h
        y += f(a)
    return y * h


def fun(x):
    return x ** 2


if __name__ == '__main__':
    # Those test might seems like hyper fast
    interval, panel = 10**2, 10**1
    test1 = time()
    newton_cotes(fun, panel, 0, interval)
    print(time() - test1)

    test2 = time()
    newton_cotes_better(fun, panel, 0, interval)
    print(time() - test2)

    # But in reality, a computer repeat far more than 10**6 operation a day
    repeat = 10**5
    t1 = time()
    for _ in range(repeat):
        newton_cotes(fun, panel, 0, interval)
    print(time() - t1)

    t2 = time()
    for _ in range(repeat):
        newton_cotes_better(fun, panel, 0, interval)
    print(time() - t2)
