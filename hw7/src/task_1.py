"""Построение min-heap двумя способами и замер времени."""
import time


def timed(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f} s")
        return result

    return wrapper


def sift_up(heap: list[int], i: int) -> None:
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break


def sift_down(arr: list[int], n: int, i: int) -> None:
    while True:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest == i:
            break

        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def makeheap_nlogn(arr: list[int]) -> list[int]:
    heap: list[int] = []
    for x in arr:
        heap.append(x)
        sift_up(heap, len(heap) - 1)
    arr[:] = heap
    return arr


def makeheap_n(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, n, i)
    return arr
