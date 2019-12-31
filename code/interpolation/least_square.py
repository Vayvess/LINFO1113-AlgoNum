import matplotlib.pyplot as plt
import numpy as np
import math


def choleski(a):
    n = len(a)
    for k in range(n):
        try:
            a[k, k] = math.sqrt(a[k, k] - np.dot(a[k, 0:k], a[k, 0:k]))
        except ValueError:
            raise Exception('Matrix is not positive definite')
        for i in range(k+1, n):
            a[i, k] = (a[i, k] - np.dot(a[i, 0:k], a[k, 0:k]))/a[k, k]
    for k in range(1, n):
        a[0:k, k] = 0.0
    return a


def choleski_sol(mx, b):
    n = len(b)
    for k in range(n):
        b[k] = (b[k] - np.dot(mx[k, 0:k], b[0:k])) / mx[k, k]

    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(mx[k + 1:n, k], b[k + 1:n])) / mx[k, k]
    return b


def poly_fit(vx, vy, poly_d):
    a = np.zeros((poly_d + 1, poly_d + 1))
    b = np.zeros(poly_d + 1)
    s = np.zeros(2 * poly_d + 1)

    for i in range(len(vx)):
        temp = vy[i]
        for j in range(poly_d + 1):
            b[j] += temp
            temp *= vx[i]
        temp = 1.0
        for j in range(2 * poly_d + 1):
            s[j] += temp
            temp *= vx[i]
    for i in range(poly_d + 1):
        for j in range(poly_d + 1):
            a[i, j] = s[i+j]
    return choleski_sol(choleski(a), b)


def get_point(x, coeffs):
    m, y = len(coeffs), 0
    for i in range(m):
        y += coeffs[i] * np.power(x, i)
    return y


def plot_poly(vx, vy, coeffs, x_lab='x', y_lab='y'):
    m = len(coeffs)
    x1, x2 = min(vx), max(vx)
    dx = (x2 - x1) / 20.0

    x, y = np.arange(x1, x2 + dx / 10.0, dx), 0
    for i in range(m):
        y += coeffs[i] * np.power(x, i)

    plt.plot(vx, vy, 'o', x, y, '-')
    plt.title(f'Using a polynomial of degree {m - 1}')
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.grid(True)
    plt.show()


xData = np.array([-4, -3, -2, -1, 1, 2, 3, 4], dtype='float')
yData = np.array([17, 10, 5, 2, 2, 5, 10, 17], dtype='float')

# Degree 1
coefficients = poly_fit(xData, yData, 1)
plot_poly(xData, yData, coefficients)

# Degree 2
coefficients = poly_fit(xData, yData, 2)
plot_poly(xData, yData, coefficients)

# The data i gave correspond to y = x² + 1
print(coefficients)
for i in range(4, 100):
    print(get_point(i, coefficients) == (i**2) + 1)

