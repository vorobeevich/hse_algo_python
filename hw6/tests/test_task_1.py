"""Тесты для рекурсивных mergesort и quicksort с замером времени."""

import random
import time
import sys

from src.task_1 import mergesort, quicksort, mergesort_timed, quicksort_timed

sys.setrecursionlimit(50000)


def test_empty_and_single_element():
    assert mergesort([]) == []
    assert quicksort([]) == []
    assert mergesort([1]) == [1]
    assert quicksort([1]) == [1]


def test_small_arrays():
    arrays = [
        [2, 1],
        [3, 1, 2],
        [5, 3, 4, 1, 2],
        [1, 1, 1],
        [2, 2, 1, 3],
    ]
    for arr in arrays:
        expected = sorted(arr)
        assert mergesort(arr) == expected
        assert quicksort(arr) == expected


def test_random_arrays_mergesort():
    random.seed(0)
    for _ in range(50):
        n = random.randint(0, 20)
        arr = [random.randint(-100, 100) for _ in range(n)]
        assert mergesort(arr) == sorted(arr)


def test_random_arrays_quicksort():
    random.seed(1)
    for _ in range(50):
        n = random.randint(0, 20)
        arr = [random.randint(-100, 100) for _ in range(n)]
        assert quicksort(arr) == sorted(arr)


def test_sorted_and_reverse_arrays():
    arr = list(range(20))
    rev = list(reversed(arr))
    expected = sorted(arr)

    assert mergesort(arr) == expected
    assert quicksort(arr) == expected
    assert mergesort(rev) == expected
    assert quicksort(rev) == expected


def test_timed_wrappers_return_correct_result():
    print("[test_timed_wrappers_return_correct_result]")
    arr = [5, 3, 1, 4, 2]
    expected = sorted(arr)

    assert mergesort_timed(arr) == expected
    assert quicksort_timed(arr) == expected


def test_large_random_array_performance():
    print("[test_large_random_array_performance]")
    n = 20000
    random.seed(42)
    arr = [random.randint(-10**6, 10**6) for _ in range(n)]

    start = time.perf_counter()
    res_merge = mergesort(arr)
    t_merge = time.perf_counter() - start

    start = time.perf_counter()
    res_quick = quicksort(arr)
    t_quick = time.perf_counter() - start

    start = time.perf_counter()
    res_sorted = sorted(arr)
    t_sorted = time.perf_counter() - start

    assert res_merge == res_sorted
    assert res_quick == res_sorted

    print(f"[test_large_random_array_performance] mergesort:      {t_merge:.6f} s")
    print(f"[test_large_random_array_performance] quicksort:      {t_quick:.6f} s")
    print(f"[test_large_random_array_performance] built-in sorted: {t_sorted:.6f} s")


def test_large_equal_array_mergesort_faster():
    print("[test_large_equal_array_mergesort_faster]")
    n = 4000
    arr = [1] * n

    start = time.perf_counter()
    res_merge = mergesort(arr)
    t_merge = time.perf_counter() - start

    start = time.perf_counter()
    res_quick = quicksort(arr)
    t_quick = time.perf_counter() - start

    start = time.perf_counter()
    res_sorted = sorted(arr)
    t_sorted = time.perf_counter() - start

    assert res_merge == res_sorted
    assert res_quick == res_sorted

    print(f"[test_large_equal_array_mergesort_faster] mergesort:      {t_merge:.6f} s")
    print(f"[test_large_equal_array_mergesort_faster] quicksort:      {t_quick:.6f} s")
    print(f"[test_large_equal_array_mergesort_faster] built-in sorted: {t_sorted:.6f} s")

    assert t_quick > t_merge