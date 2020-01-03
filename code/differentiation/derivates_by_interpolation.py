import matplotlib.pyplot as plt
import numpy as np


def choleski(a):
    n = len(a)
    for k in range(n):
        try:
            a[k, k] = np.sqrt(a[k, k] - np.dot(a[k, 0:k], a[k, 0:k]))
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


def least_square(vx, vy, poly_d):
    class Polynomial:
        def __init__(self, coefficients):
            self.coefficients = coefficients

        def __call__(self, x):
            y = 0
            for index, coefficient in enumerate(self.coefficients):
                y += coefficient * np.power(x, index)
            return y

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
    return Polynomial(choleski_sol(choleski(a), b))


def least_square_df(f):
    class PolynomialDerivative:
        def __init__(self, coefficients):
            self.coefficients = []
            for i in range(1, len(coefficients)):
                self.coefficients.append(coefficients[i] * i)

        def __call__(self, x):
            y = 0
            for i, coefficient in enumerate(self.coefficients):
                y += coefficient * np.power(x, i)
            return y

    vx = np.arange(-5, 6, 1)
    vy = np.vectorize(f)(vx)
    return PolynomialDerivative(least_square(vx, vy, 6).coefficients)


def plot_func_and_derivative(f, n):
    vx = np.arange(-n, n + 1, 1)
    f_vy = np.vectorize(f)(vx)
    df_vy = np.vectorize(least_square_df(f))(vx)
    plt.plot(vx, f_vy, '-', vx, df_vy, 'o')
    plt.title('Polynomial function and its derivative')
    plt.grid(True)
    plt.show()


plot_func_and_derivative(lambda x: x**2, 15)

size, fun = 5, lambda x: x**3
x_data = np.array([i for i in range(-size, size + 1, 1)])
y_data = np.vectorize(fun)(x_data)

x_cube = least_square(x_data, y_data, 3)
for abscissa in range(0, 100):
    assert(x_cube(abscissa) == abscissa ** 3)

three_x_square = least_square_df(fun)
for abscissa in range(0, 100):
    assert (three_x_square(abscissa) == 3 * abscissa ** 2)
