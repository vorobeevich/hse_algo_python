"""Ищет индексы двух элементов массива, сумма которых равна k."""


def two_sum(arr: list[int], k: int) -> tuple[int, int]:
    seen: dict[int, int] = {}

    for i, x in enumerate(arr):
        need = k - x
        if need in seen:
            j = seen[need]
            return tuple(sorted((j, i)))
        seen[x] = i