def recursive_trapezoid(f, a, b, n=16):
    h, sigma = (b - a) / n, 0.5 * (f(a) + f(b))
    for i in range(1, n):
        sigma += f(a + i * h)
    return h * sigma


def fun(x):
    return x**2 + 2 * x + 2


def integral_of_fun(x):
    return x**3 / 3 + x**2 + 2 * x


x1, x2, n_times = 0, 3, 3
print(recursive_trapezoid(fun, x1, x2, n_times))
ix1, ix2 = integral_of_fun(x1), integral_of_fun(x2)
print(ix2 - ix1)
