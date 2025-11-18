"""Тесты для итеративных mergesort и quicksort."""

import random
import time

from src.task_2 import iterative_mergesort, iterative_quicksort


def test_empty_and_single_element():
    assert iterative_mergesort([]) == []
    assert iterative_quicksort([]) == []
    assert iterative_mergesort([1]) == [1]
    assert iterative_quicksort([1]) == [1]


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
        assert iterative_mergesort(arr) == expected
        assert iterative_quicksort(arr) == expected


def test_random_arrays_iterative_mergesort():
    random.seed(0)
    for _ in range(50):
        n = random.randint(0, 20)
        arr = [random.randint(-100, 100) for _ in range(n)]
        assert iterative_mergesort(arr) == sorted(arr)


def test_random_arrays_iterative_quicksort():
    random.seed(1)
    for _ in range(50):
        n = random.randint(0, 20)
        arr = [random.randint(-100, 100) for _ in range(n)]
        assert iterative_quicksort(arr) == sorted(arr)


def test_sorted_and_reverse_arrays():
    arr = list(range(20))
    rev = list(reversed(arr))
    expected = sorted(arr)

    assert iterative_mergesort(arr) == expected
    assert iterative_quicksort(arr) == expected
    assert iterative_mergesort(rev) == expected
    assert iterative_quicksort(rev) == expected


def test_original_array_not_modified():
    arr = [3, 1, 2, 5, 4]
    copy1 = arr[:]
    copy2 = arr[:]

    iterative_mergesort(arr)
    iterative_quicksort(arr)

    assert arr == copy1 == copy2


def test_large_random_array_performance_iterative():
    print("[test_large_random_array_performance_iterative]")
    n = 20000
    random.seed(42)
    arr = [random.randint(-10**6, 10**6) for _ in range(n)]

    start = time.perf_counter()
    res_merge = iterative_mergesort(arr)
    t_merge = time.perf_counter() - start

    start = time.perf_counter()
    res_quick = iterative_quicksort(arr)
    t_quick = time.perf_counter() - start

    start = time.perf_counter()
    res_sorted = sorted(arr)
    t_sorted = time.perf_counter() - start

    assert res_merge == res_sorted
    assert res_quick == res_sorted

    print(f"[test_large_random_array_performance_iterative] mergesort:      {t_merge:.6f} s")
    print(f"[test_large_random_array_performance_iterative] quicksort:      {t_quick:.6f} s")
    print(f"[test_large_random_array_performance_iterative] built-in sorted: {t_sorted:.6f} s")


def test_large_equal_array_mergesort_faster_iterative():
    print("[test_large_equal_array_mergesort_faster_iterative]")
    n = 4000
    arr = [1] * n

    start = time.perf_counter()
    res_merge = iterative_mergesort(arr)
    t_merge = time.perf_counter() - start

    start = time.perf_counter()
    res_quick = iterative_quicksort(arr)
    t_quick = time.perf_counter() - start

    start = time.perf_counter()
    res_sorted = sorted(arr)
    t_sorted = time.perf_counter() - start

    assert res_merge == res_sorted
    assert res_quick == res_sorted

    print(f"[test_large_equal_array_mergesort_faster_iterative] mergesort:      {t_merge:.6f} s")
    print(f"[test_large_equal_array_mergesort_faster_iterative] quicksort:      {t_quick:.6f} s")
    print(f"[test_large_equal_array_mergesort_faster_iterative] built-in sorted: {t_sorted:.6f} s")

    assert t_quick > t_merge
