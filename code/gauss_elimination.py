import numpy as np


def gauss_elimination(a, b):
    n = len(b)
    # Elimination phase
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[j, i] != 0.0:
                lam = a[j, i] / a[i, i]
                a[j, i + 1:n] -= lam * a[i, i + 1:n]
                b[j] -= lam * b[i]

    # Back substitution
    for i in range(n-1, -1, -1):
        b[i] -= a[i, i + 1:n] @ b[i + 1:n]
        b[i] /= a[i, i]
    return b


A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], dtype='float')
b = np.array([-3, -1, 4], dtype='float')
print(gauss_elimination(A, b))
