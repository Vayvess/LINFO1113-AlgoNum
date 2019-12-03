import numpy as np


def lu_dec(mx):
    n = len(mx)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if mx[j, i]:
                lam = mx[j, i] / mx[i, i]
                mx[j, i + 1:n] -= lam * mx[i, i + 1:n]
                mx[j, i] = lam
    return mx


def lu_solve(a, b):
    n = len(a)
    # LY=B forward substitution
    for k in range(1, n):
        b[k] -= a[k, 0:k] @ b[0:k]
    # UX=Y backward substitution
    b[n - 1] /= a[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        b[k] -= a[k, k + 1:n] @ b[k + 1:n]
        b[k] /= a[k, k]
    return b


A = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]], dtype='float')
b = np.array([-3, -1, 4], dtype='float')
lu = lu_dec(A)
print(lu_solve(lu, b))

