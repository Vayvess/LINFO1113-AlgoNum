import numpy as np


def bracket(f, x1, h):
    c, f1 = 1.618033989, f(x1)
    x2, f2 = x1 + h, f(x1 + h)

    # Determine downhill direction and change sign of h if needed
    if f2 > f1:
        h = -h
        x2, f2 = x1 + h, f(x1 + h)
        if f2 > f1:
            return x2, x1 - h

    # search loop
    for i in range(100):
        h *= c
        x3, f3 = x2 + h, f(x2 + h)
        if f3 > f2:
            return x1, x3
        x1, x2, f1, f2 = x2, x3, f2, f3
    print("Bracket didn't find a minimum")


def func(x):
    return x**2 - 4 * x


print(bracket(func, 2, 0.5))
