def composite_simpson(f, n, a, b):
    h, y = (b - a) / n, f(a) + f(b)
    for i in range(n - 1):
        a += h
        y += f(a) * 2 if i % 2 else f(a) * 4
    return (y * h) / 3


def fun(x):
    return x**2 + 2 * x + 2


def integral_of_fun(x):
    return x**3 / 3 + x**2 + 2 * x


if __name__ == '__main__':
    x1, x2, n_times = 0, 9, 4
    print(composite_simpson(fun, n_times, x1, x2))
    ix1, ix2 = integral_of_fun(x1), integral_of_fun(x2)
    print(ix2 - ix1)
