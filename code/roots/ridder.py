import math
import numpy as np


def ridder(f, a, b, tol=1.0e-9):
    fa, fb = f(a), f(b)
    c = 0.5 * (a + b)
    fc = f(c)
    s = np.sqrt(np.power(fc, 2) - fa * fb)
    if s:
        dx = (c - a) * fc / s
        if fa - fb < 0.0:
            dx = -dx
        x = c + dx
        fx = f(x)
