import math
import numpy as np


def choleski(a):
    n = len(a)
    for k in range(n):
        try:
            a[k, k] = math.sqrt(a[k, k] - np.dot(a[k, 0:k], a[k, 0:k]))
        except ValueError:
            raise Exception('Matrix is not positive definite')
        for i in range(k + 1, n):
            a[i, k] = (a[i, k] - np.dot(a[i, 0:k], a[k, 0:k])) / a[k, k]
    for k in range(1, n):
        a[0:k, k] = 0.0
    return a


def choleski_sol(L, b):
    n = len(b)
    for k in range(n):
        b[k] = (b[k] - np.dot(L[k, 0:k], b[0:k])) / L[k, k]
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(L[k+1:n, k], b[k+1:n])) / L[k, k]
    return b


# Note on the slides he forgot to settle the type of the numpy array to float
A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]], dtype='float')

b = np.array([-3, -1, 4], dtype='float')
L = choleski(A)
print(L, '\n')
result = choleski_sol(L, b)
print(result)
