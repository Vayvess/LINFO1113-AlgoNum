import math
import numpy as np


def root_search(f, a, b, dx=1.e-2):
    x1, f1 = a, f(a)
    x2, f2 = a + dx, f(a + dx)
    while x1 < b:
        if np.sign(f1) != np.sign(f2):
            return x1, x2
        x1, f1 = x2, f2
        x2, f2 = x1 + dx, f(x1 + dx)
    return None, None
