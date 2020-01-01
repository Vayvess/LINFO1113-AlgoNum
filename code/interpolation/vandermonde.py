import numpy as np
import matplotlib.pyplot as plt


def jacobi(a, tol=0.1e-8):
    def distance(curr, old):
        w = curr - old
        return np.dot(w, w).sum()

    n = len(a)
    x, prev = np.zeros(n), np.ones(n)
    while distance(x, prev) > tol:
        prev = x.copy()
        for i in range(n):
            sigma = 0
            for j in range(n):
                if i != j:
                    sigma += a[i, j] * x[j]
            x[i] = (1 / a[i, i]) * (a[i, -1] - sigma)
    return x


def vandermonde(vx, vy):
    n = len(vx)
    mx = np.zeros(shape=(n, n + 1), dtype=float)
    for i in range(n):
        row = np.zeros(n + 1, dtype=float)
        for j in range(n):
            row[j] = np.power(vx[i], j)
        row[n] = vy[i]
        mx[i] = row
    return jacobi(mx)


def get_y(x, coeffs):
    n, sigma = len(coeffs), 0
    for i in range(n):
        sigma += coeffs[i] * np.power(x, i)
    return sigma


def get_data_sets(start=-5, end=5, step=0.1):
    x_set = np.arange(start, end, step)
    return x_set, np.array([get_y(p, coefficients) for p in x_set])


# constraints
u = np.array([0, 2, 4], dtype=float)
v = np.array([1, 4, 16], dtype=float)

# computing
coefficients = vandermonde(u, v)
x_data_set, y_data_set = get_data_sets()

# plotting
plt.plot(x_data_set, y_data_set)
for px, py in zip(u, v):
    plt.plot(px, py, 'go')
plt.show()
