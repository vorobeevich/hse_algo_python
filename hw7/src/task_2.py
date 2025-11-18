"""Поиск k-го по величине с помощью min-heap (свой и heapq)."""

import heapq


class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, x: int):
        data = self.data
        data.append(x)
        i = len(data) - 1
        while i > 0:
            parent = (i - 1) // 2
            if data[i] < data[parent]:
                data[i], data[parent] = data[parent], data[i]
                i = parent
            else:
                break

    def pop(self) -> int:
        data = self.data

        result = data[0]
        last = data.pop()
        if data:
            data[0] = last
            i = 0
            n = len(data)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                smallest = i

                if left < n and data[left] < data[smallest]:
                    smallest = left
                if right < n and data[right] < data[smallest]:
                    smallest = right

                if smallest == i:
                    break

                data[i], data[smallest] = data[smallest], data[i]
                i = smallest
        return result

    def top(self) -> int:
        return self.data[0]

    def __len__(self) -> int:
        return len(self.data)


def kth_largest_heap(nums: list[int], k: int) -> int:
    heap = MinHeap()

    for x in nums:
        if len(heap) < k:
            heap.push(x)
        elif x > heap.top():
            heap.pop()
            heap.push(x)

    return heap.top()


def kth_largest_heapq(nums: list[int], k: int) -> int:
    heap = nums[:k]
    heapq.heapify(heap)

    for x in nums[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)

    return heap[0]