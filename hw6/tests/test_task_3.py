"""Тесты для quickselect (k-й по величине элемент)."""

import random

from src.task_3 import quickselect


def test_single_element():
    assert quickselect([5], 1) == 5


def test_simple_cases():
    arr = [3, 1, 2, 4]
    assert quickselect(arr, 1) == 4 
    assert quickselect(arr, 2) == 3
    assert quickselect(arr, 3) == 2
    assert quickselect(arr, 4) == 1


def test_with_duplicates():
    arr = [3, 1, 2, 2, 4]
    assert quickselect(arr, 1) == 4
    assert quickselect(arr, 2) == 3
    assert quickselect(arr, 3) == 2
    assert quickselect(arr, 4) == 2
    assert quickselect(arr, 5) == 1


def test_negative_numbers():
    arr = [-5, -1, -3, 0, 2]
    assert quickselect(arr, 1) == 2
    assert quickselect(arr, 3) == -1
    assert quickselect(arr, 5) == -5


def test_original_array_not_modified():
    arr = [7, 4, 6, 3, 9, 1]
    copy = arr[:]
    _ = quickselect(arr, 2)
    assert arr == copy


def test_random_arrays_against_sorted():
    random.seed(0)
    for _ in range(100):
        n = random.randint(1, 50)
        arr = [random.randint(-1000, 1000) for _ in range(n)]
        k = random.randint(1, n)

        expected = sorted(arr, reverse=True)[k - 1]
        assert quickselect(arr, k) == expected
