import numpy as np


def segment(a, b, n):
    h = (b - a) / n
    np.arange(a, b, h)
