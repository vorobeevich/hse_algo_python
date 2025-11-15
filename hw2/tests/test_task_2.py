"""Тесты для validate_stack_sequences."""

from src.task_2 import validate_stack_sequences


def test_example_true():
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 5, 4, 2]
    assert validate_stack_sequences(pushed, popped)


def test_example_false():
    pushed = [1, 2, 3]
    popped = [3, 1, 2]
    assert not validate_stack_sequences(pushed, popped)


def test_same_order():
    pushed = [1, 2, 3, 4]
    popped = [1, 2, 3, 4]
    assert validate_stack_sequences(pushed, popped)


def test_reverse_order():
    pushed = [1, 2, 3, 4]
    popped = [4, 3, 2, 1]
    assert validate_stack_sequences(pushed, popped)


def test_valid_interleaving():
    pushed = [1, 2, 3, 4, 5]
    popped = [2, 1, 4, 3, 5]
    assert validate_stack_sequences(pushed, popped)


def test_invalid_pattern():
    pushed = [1, 2, 3, 4]
    popped = [3, 1, 4, 2]
    assert not validate_stack_sequences(pushed, popped)


def test_single_element_true():
    assert validate_stack_sequences([1], [1])


def test_length_mismatch_shorter_popped():
    assert not validate_stack_sequences([1, 2, 3], [1, 2])


def test_length_mismatch_longer_popped():
    assert not validate_stack_sequences([1, 2], [1, 2, 3])


def test_not_a_permutation_different_element():
    pushed = [1, 2, 3]
    popped = [1, 2, 4]
    assert not validate_stack_sequences(pushed, popped)


def test_not_a_permutation_duplicate_in_popped():
    pushed = [1, 2, 3]
    popped = [1, 1, 2]
    assert not validate_stack_sequences(pushed, popped)


def test_large_reverse_order():
    pushed = list(range(1, 1000))
    popped = list(reversed(pushed))
    assert validate_stack_sequences(pushed, popped)