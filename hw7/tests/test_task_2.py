"""Тесты для поиска k-го по величине через min-heap."""

import random

from src.task_2 import kth_largest_heap, kth_largest_heapq


def ground_truth(nums: list[int], k: int) -> int:
    return sorted(nums, reverse=True)[k - 1]


def test_single_element():
    nums = [5]
    k = 1
    expected = 5
    assert kth_largest_heap(nums, k) == expected
    assert kth_largest_heapq(nums, k) == expected


def test_examples_from_statement():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    expected = 5
    assert kth_largest_heap(nums, k) == expected
    assert kth_largest_heapq(nums, k) == expected

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    expected = 4
    assert kth_largest_heap(nums, k) == expected
    assert kth_largest_heapq(nums, k) == expected


def test_with_duplicates():
    nums = [5, 5, 5, 5]
    assert kth_largest_heap(nums, 1) == 5
    assert kth_largest_heap(nums, 2) == 5
    assert kth_largest_heap(nums, 3) == 5
    assert kth_largest_heap(nums, 4) == 5

    assert kth_largest_heapq(nums, 1) == 5
    assert kth_largest_heapq(nums, 2) == 5
    assert kth_largest_heapq(nums, 3) == 5
    assert kth_largest_heapq(nums, 4) == 5


def test_negative_and_mixed():
    nums = [-1, -5, 0, 3, 2]
    for k in range(1, len(nums) + 1):
        expected = ground_truth(nums, k)
        assert kth_largest_heap(nums, k) == expected
        assert kth_largest_heapq(nums, k) == expected


def test_random_arrays_against_sorted():
    random.seed(0)
    for _ in range(100):
        n = random.randint(1, 50)
        nums = [random.randint(-1000, 1000) for _ in range(n)]
        k = random.randint(1, n)
        expected = ground_truth(nums, k)

        assert kth_largest_heap(nums, k) == expected
        assert kth_largest_heapq(nums, k) == expected