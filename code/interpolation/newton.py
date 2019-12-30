import math
import numpy as np
import matplotlib.pyplot as plt


def coefficients(x_data, y_data):
    m = len(x_data)
    a = y_data.copy()
    for k in range(1, m):
        a[k:m] = (a[k:m] - a[k-1]) / (x_data[k:m] - x_data[k-1])
    return a


def eval_poly(a, x_data, x):
    n = len(x_data) - 1
    p = a[n]
    for k in range(1, n + 1):
        p = a[n - k] + (x - x_data[n - k]) * p
    return p


x_data_set = np.array([-2, 1, 4, -1, 3, -4], dtype='float')
y_data_set = np.array([-1, 2, 59, 4, 24, -53], dtype='float')

coeffs = coefficients(x_data_set, y_data_set)
print(coeffs)
print(eval_poly(coeffs, x_data_set, 4))