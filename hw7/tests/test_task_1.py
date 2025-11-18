"""Тесты для построения min-heap двумя способами."""
import random
import time

from src.task_1 import makeheap_nlogn, makeheap_n


def is_min_heap(arr: list[int]) -> bool:
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True


def check_heap_build(arr: list[int]) -> None:
    original = arr[:]

    a1 = arr[:]
    a2 = arr[:]

    makeheap_nlogn(a1)
    makeheap_n(a2)

    assert is_min_heap(a1)
    assert is_min_heap(a2)
    assert sorted(a1) == sorted(original)
    assert sorted(a2) == sorted(original)


def test_empty_and_single_element():
    check_heap_build([])
    check_heap_build([5])


def test_small_arrays():
    arrays = [
        [3, 1, 2],
        [2, 1],
        [5, 3, 4, 1, 2],
        [1, 1, 1],
        [4, 2, 2, 3],
    ]
    for arr in arrays:
        check_heap_build(arr)


def test_random_arrays_small():
    random.seed(0)
    for _ in range(50):
        n = random.randint(0, 30)
        arr = [random.randint(-100, 100) for _ in range(n)]
        check_heap_build(arr)


def test_large_random_array_performance():
    print("[test_large_random_array_performance]")
    n = 10_000_000
    random.seed(42)
    arr = [random.randint(-10**6, 10**6) for _ in range(n)]

    a1 = arr[:]
    a2 = arr[:]

    start = time.perf_counter()
    makeheap_nlogn(a1)
    t_nlogn = time.perf_counter() - start

    start = time.perf_counter()
    makeheap_n(a2)
    t_n = time.perf_counter() - start

    assert is_min_heap(a1)
    assert is_min_heap(a2)
    assert sorted(a1) == sorted(arr)
    assert sorted(a2) == sorted(arr)

    print(f"[test_large_random_array_performance] makeheap_nlogn: {t_nlogn:.6f} s")
    print(f"[test_large_random_array_performance] makeheap_n:     {t_n:.6f} s")