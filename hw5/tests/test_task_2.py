"""Тесты для permutations."""

import itertools
import random

from src.task_2 import permutations


def normalize(perms: list[list[int]]) -> list[list[int]]:
    return sorted(perms)


def test_single_element():
    nums = [1]
    assert permutations(nums) == [[1]]


def test_two_elements():
    nums = [0, 1]
    res = normalize(permutations(nums))
    expected = normalize([[0, 1], [1, 0]])
    assert res == expected


def test_example_three_elements():
    nums = [1, 2, 3]
    res = normalize(permutations(nums))
    expected = normalize(
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    )
    assert res == expected


def test_random_against_itertools():
    random.seed(0)
    for _ in range(10):
        n = random.randint(1, 5)
        nums = random.sample(range(10), n)

        res = normalize(permutations(nums))
        expected = normalize([list(p) for p in itertools.permutations(nums)])

        assert res == expected