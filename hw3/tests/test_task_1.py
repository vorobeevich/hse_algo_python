"""Тесты для two_sum."""

import random

from src.task_1 import two_sum


def test_simple_case():
    arr = [2, 7, 11, 15]
    k = 9
    assert two_sum(arr, k) == (0, 1)


def test_pair_not_adjacent():
    arr = [1, 4, 5, 11]
    k = 6
    assert two_sum(arr, k) == (0, 2)


def test_with_negative_numbers():
    arr = [-3, 1, 4, 2]
    k = -1
    assert two_sum(arr, k) == (0, 3)


def test_with_zero():
    arr = [0, 4, 3, 0]
    k = 0
    assert two_sum(arr, k) == (0, 3)


def test_duplicates_same_value():
    arr = [3, 1, 3]
    k = 6
    assert two_sum(arr, k) == (0, 2)


def test_min_length_two():
    arr = [5, -2]
    k = 3
    assert two_sum(arr, k) == (0, 1)


def test_pair_at_end():
    arr = [10, 20, 30, 40]
    k = 70
    assert two_sum(arr, k) == (2, 3)


def test_random_shuffles_single_pair():
    base = [1, 3, 5, 7]
    k = 10

    random.seed(0)
    for _ in range(100):
        arr = base[:]
        random.shuffle(arr)
        i, j = two_sum(arr, k)
        assert i < j
        assert arr[i] + arr[j] == k