"""Простая хеш-таблица на списках с методами put, get, delete."""


class HashTable:
    def __init__(self, initial_capacity: int = 8):
        self._buckets: list[list[list]] = [[] for _ in range(initial_capacity)]
        self._size: int = 0

    def _bucket_index(self, key) -> int:
        return hash(key) % len(self._buckets)

    def _resize(self):
        new_capacity = len(self._buckets) * 2
        new_buckets: list[list[list]] = [[] for _ in range(new_capacity)]

        for bucket in self._buckets:
            for key, value in bucket:
                index = hash(key) % new_capacity
                new_buckets[index].append([key, value])

        self._buckets = new_buckets

    def put(self, key, value):
        index = self._bucket_index(key)
        bucket = self._buckets[index]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])
        self._size += 1

        if self._size / len(self._buckets) > 0.75:
            self._resize()

    def get(self, key):
        index = self._bucket_index(key)
        bucket = self._buckets[index]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        raise KeyError(key)

    def delete(self, key):
        index = self._bucket_index(key)
        bucket = self._buckets[index]

        for i, pair in enumerate(bucket):
            if pair[0] == key:
                value = pair[1]
                del bucket[i]
                self._size -= 1
                return value

        raise KeyError(key)

    def __len__(self) -> int:
        return self._size