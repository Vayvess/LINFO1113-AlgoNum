def memoize(f):
    def wrapper(**kwargs):
        print(kwargs)
    return wrapper


def dfn(g, x, n, h=1e-8):
    return (g(x + h) - g(x - h)) / (2 * h) if n == 1 else (dfn(g, x + h, n - 1) - dfn(g, x - h, n - 1, h)) / (2 * h)


@memoize
def gun(x):
    return 2 * x


gun(test=5)

