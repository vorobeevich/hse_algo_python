"""Тесты для task_1.is_palindrome."""

import random

from src.task_1 import is_palindrome


def is_palindrome_str(n: int) -> bool:
    s = str(n)
    return s == s[::-1]


def test_single_digit_palindrome():
    assert is_palindrome(7)


def test_simple_palindrome():
    assert is_palindrome(121)


def test_simple_non_palindrome():
    assert not is_palindrome(12)


def test_number_with_trailing_zeros():
    assert not is_palindrome(10)
    assert not is_palindrome(100)


def test_zero():
    assert not is_palindrome(0)


def test_number_from_leading_zeros_string():
    n = int("010")
    assert n == 10
    assert not is_palindrome(n)


def test_random_numbers_against_string_impl():
    random.seed(0)
    for _ in range(1000):
        n = random.randint(1, 10**9)
        assert is_palindrome(n) == is_palindrome_str(n)