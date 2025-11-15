"""Тесты для task_2.max_even_sum."""

from src.task_2 import max_even_sum


def test_all_even():
    assert max_even_sum([2, 4, 6]) == 12


def test_mixed_total_even():
    assert max_even_sum([1, 2, 3]) == 6


def test_mixed_need_drop_min_odd():
    assert max_even_sum([1, 2, 4]) == 6


def test_single_odd():
    assert max_even_sum([5]) == 0


def test_single_even():
    assert max_even_sum([8]) == 8


def test_all_odds_even_count():
    assert max_even_sum([1, 3]) == 4


def test_all_odds_odd_count():
    assert max_even_sum([1, 3, 5]) == 8


def test_unsorted_mixed():
    assert max_even_sum([7, 2, 5, 4]) == 18


def test_large_numbers():
    assert max_even_sum([10**9 - 1, 10**9]) == 10**9


def test_empty_list():
    assert max_even_sum([]) == 0