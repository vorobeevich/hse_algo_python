"""Итеративные версии mergesort и quicksort."""

import random


def iterative_mergesort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n <= 1:
        return arr[:]

    res = arr[:]
    tmp = [0] * n
    width = 1

    while width < n:
        for left in range(0, n, 2 * width):
            mid = min(left + width, n)
            right = min(left + 2 * width, n)

            i = left
            j = mid
            k = left

            while i < mid and j < right:
                if res[i] <= res[j]:
                    tmp[k] = res[i]
                    i += 1
                else:
                    tmp[k] = res[j]
                    j += 1
                k += 1

            while i < mid:
                tmp[k] = res[i]
                i += 1
                k += 1

            while j < right:
                tmp[k] = res[j]
                j += 1
                k += 1

        res, tmp = tmp, res
        width *= 2

    return res


def iterative_quicksort(arr: list[int]) -> list[int]:
    n = len(arr)
    if n <= 1:
        return arr[:]

    res = arr[:]
    stack = [(0, n - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot_index = random.randint(left, right)
        res[pivot_index], res[right] = res[right], res[pivot_index]
        pivot = res[right]

        i = left
        for j in range(left, right):
            if res[j] <= pivot:
                res[i], res[j] = res[j], res[i]
                i += 1

        res[i], res[right] = res[right], res[i]

        if left < i - 1:
            stack.append((left, i - 1))
        if i + 1 < right:
            stack.append((i + 1, right))

    return res
