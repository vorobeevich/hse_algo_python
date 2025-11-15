"""Вычисляет максимальную чётную сумму элементов массива. Ответ это либа сумма всего массива, либо вычитаем минимальный нечетный элемент."""


from typing import List


def max_even_sum(nums: List[int]) -> int:
    total = sum(nums)
    if total % 2 == 0:
        return total

    min_odd = None
    for x in nums:
        if x % 2 == 1 and (min_odd is None or x < min_odd):
            min_odd = x

    if min_odd is None:
        return 0

    return total - min_odd