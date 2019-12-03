from time import time


def benchmark(f):
    def wrapper(*args, **kwargs):
        t1 = time()
        ans = f(*args, **kwargs)
        return f'Time taken: {time() - t1}'
    return wrapper
