"""Тесты для task_3.count_primes."""

import random

from src.task_3 import count_primes


def count_primes_slow(n: int) -> int:
    def is_prime(k: int) -> bool:
        if k < 2:
            return False
        if k == 2:
            return True
        if k % 2 == 0:
            return False
        d = 3
        while d * d <= k:
            if k % d == 0:
                return False
            d += 2
        return True

    return sum(1 for x in range(n) if is_prime(x))


def test_small_n():
    assert count_primes(0) == 0
    assert count_primes(1) == 0
    assert count_primes(2) == 0
    assert count_primes(3) == 1
    assert count_primes(4) == 2


def test_values_around_boundaries():
    assert count_primes(10) == 4
    assert count_primes(11) == 4
    assert count_primes(12) == 5


def test_known_values():
    assert count_primes(100) == 25
    assert count_primes(1000) == 168


def test_random_against_slow():
    random.seed(0)
    for _ in range(50):
        n = random.randint(0, 1000)
        assert count_primes(n) == count_primes_slow(n)
