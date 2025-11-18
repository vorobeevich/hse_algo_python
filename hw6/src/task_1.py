"""Рекурсивные mergesort и quicksort с декоратором для замера времени."""

import time
import random


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f} s")
        return result

    return wrapper


def mergesort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    i = 0
    j = 0
    res: list[int] = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i < len(left):
        res.extend(left[i:])
    if j < len(right):
        res.extend(right[j:])

    return res


def quicksort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n <= 1:
        return arr

    pivot_index = random.randrange(n)
    pivot = arr[pivot_index]

    less: list[int] = []
    greater: list[int] = []

    for i, x in enumerate(arr):
        if i == pivot_index:
            continue
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)

    return quicksort(less) + [pivot] + quicksort(greater)


@timed
def mergesort_timed(arr: list[int]) -> list[int]:
    return mergesort(arr)


@timed
def quicksort_timed(arr: list[int]) -> list[int]:
    return quicksort(arr)