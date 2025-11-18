"""Поиск k-го по величине элемента массива с помощью quickselect."""

import random


def quickselect(arr: list[int], k: int) -> int:
    n = len(arr)
    target = n - k
    a = arr[:]

    left = 0
    right = n - 1

    while True:
        if left == right:
            return a[left]

        pivot_index = random.randint(left, right)
        pivot = a[pivot_index]
        a[pivot_index], a[right] = a[right], a[pivot_index]

        i = left
        for j in range(left, right):
            if a[j] < pivot:
                a[i], a[j] = a[j], a[i]
                i += 1

        a[i], a[right] = a[right], a[i]
        p = i

        if target == p:
            return a[p]
        if target < p:
            right = p - 1
        else:
            left = p + 1
