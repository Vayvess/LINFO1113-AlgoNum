# Implementation by Barghest, Results aren't satisfying :/
from time import time
from random import randint
from multiprocessing import Pool
import numpy as np


def benchmark(f):
    def wrapper(*args, **kwargs):
        start = time()
        f(*args, **kwargs)
        return f'{f.__name__} has taken {(time() - start)} runtime in secs'

    return wrapper


@benchmark
def merge_this(left, right):
    output, i = [0 for _ in range(len(left) + len(right))], len(left) + len(right) - 1
    while left and right:
        output[i], i = left.pop() if left[-1] > right[-1] else right.pop(), i - 1

    reminder = left if left else right
    while reminder:
        output[i], i = reminder.pop(), i - 1
    return output


def merge_sort_this(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    return merge_this(merge_sort_this(array[:mid]), merge_sort_this(array[mid:]))


@benchmark
def merge(left, right):
    output = []
    while left and right:
        output.append(left.pop() if left[-1] < right[-1] else right.pop())
    reminder = left if left else right
    while reminder:
        output.append(reminder.pop())
    return output


def sort(arr, ascend=True):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left, right = sort(arr[:mid], not ascend), sort(arr[mid:], not ascend)
    return merge(left, right, ascend)


def merge_sort(array, ascending):
    return sort(array, ascending)


@benchmark
def merge_iter(left, right):
    i, j, output = 0, 0, []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1
    reminder, k = (left, i) if i < len(left) else (right, j)
    while k < len(reminder):
        output.append(reminder[k])
        k += 1
    return output


def sort_iter(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    return merge_iter(sort_iter(array[:mid]), sort_iter(array[mid:]))


def merge_sort_iter(array):
    return sort_iter(array)


# n_threads mut be pair
def merge_sort_threaded(array, n_threads):
    def merge_processes(processes, ascend):
        if len(processes) == 1:
            return processes.pop()
        mid = len(processes) // 2
        left, right = merge_processes(processes[:mid], not ascend), merge_processes(processes[mid:], not ascend)
        return merge(left, right, ascend)

    with Pool(processes=n_threads) as pool:
        return merge_processes(pool.map(sort, [array[i:: n_threads] for i in range(n_threads)]), True)


def rand_arr(n):
    return [randint(1, 999) for _ in range(n)]


if __name__ == '__main__':
    k = 100000
    a = [i + randint(0, 1) for i in range(k)]
    b = [i + randint(0, 1) for i in range(k)]
    print(merge_this(a, b))
    a = [i + randint(0, 1) for i in range(k)]
    b = [i + randint(0, 1) for i in range(k)]
    print(merge(a, b))
    a = [i + randint(0, 1) for i in range(k)]
    b = [i + randint(0, 1) for i in range(k)]
    print(merge_iter(a, b))
    a = np.array(a, dtype="int32")
    b = np.array(b, dtype="int32")
    print(merge_iter(a, b))
