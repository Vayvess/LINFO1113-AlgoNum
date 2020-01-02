# Implementation by Barghest, Results aren't satisfying :/

from time import time
from random import randint
from multiprocessing import Pool


def benchmark(f):
    def wrapper(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        return f'{f.__name__} has taken {(time() - start)} runtime in secs'
    return wrapper


@benchmark
def merge_sort_me(array):
    def merge(left, right, ascend):
        output = []
        while left and right:
            output.append(left.pop() if (left[-1] < right[-1] if ascend else left[-1] > right[-1]) else right.pop())
        reminder = left if left else right
        while reminder:
            output.append(reminder.pop())
        return output

    def sort(arr, ascend):
        if len(arr) < 2:
            return arr
        mid = len(arr) // 2
        left, right = sort(arr[:mid], not ascend), sort(arr[mid:], not ascend)
        return merge(left, right, ascend)

    return sort(array, True)


@benchmark
def merge_sort(array):
    def merge_iterative(left, right):
        if not len(left) or not len(right):
            return left or right

        result = []
        i, j = 0, 0
        while len(result) < len(left) + len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            if i == len(left) or j == len(right):
                result.extend(left[i:] or right[j:])
                break

        return result

    def sort_iterative(arr):
        if len(arr) < 2:
            return arr

        middle = len(arr) // 2
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge_iterative(left, right)

    return sort_iterative(array)


def merge_thread(left, right, ascend=True):
    output = []
    while left and right:
        output.append(left.pop() if (left[-1] < right[-1] if ascend else left[-1] > right[-1]) else right.pop())
    reminder = left if left else right
    while reminder:
        output.append(reminder.pop())
    return output


def sort_threaded(arr, ascend=False):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = sort_threaded(arr[:mid], not ascend), sort_threaded(arr[mid:], not ascend)
    return merge_thread(left, right, ascend)


@benchmark
def merge_sort_threaded(array, n_threads):
    with Pool(processes=n_threads) as pool:
        output = pool.map(sort_threaded, [array[i:: n_threads] for i in range(n_threads)])
        while len(output) != 1:
            output = [merge_thread(*output[i:i + 2]) for i in range(0, len(output), 2)]
        return output


def rand_arr(n):
    return [randint(1, 999) for _ in range(n)]


if __name__ == '__main__':
    testing = rand_arr(1000)
    print(merge_sort(testing))
    print(merge_sort_me(testing))
    print(merge_sort_threaded(testing, 2))
    print(merge_sort_threaded(testing, 4))
