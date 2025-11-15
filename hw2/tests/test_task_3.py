"""Тесты для слияния двух отсортированных списков."""

import random

from src.task_3 import ListNode, merge_with_fake, merge_without_fake


def list_to_linked(values):
    head = None
    tail = None
    for v in values:
        node = ListNode(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head


def linked_to_list(node):
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    return result


def merge_and_list(func, list1, list2):
    head = func(list_to_linked(list1), list_to_linked(list2))
    return linked_to_list(head)


def test_both_empty():
    assert merge_and_list(merge_with_fake, [], []) == []
    assert merge_and_list(merge_without_fake, [], []) == []


def test_one_empty_left():
    a = []
    b = [1, 2, 3]
    expected = [1, 2, 3]
    assert merge_and_list(merge_with_fake, a, b) == expected
    assert merge_and_list(merge_without_fake, a, b) == expected


def test_one_empty_right():
    a = [1, 2, 3]
    b = []
    expected = [1, 2, 3]
    assert merge_and_list(merge_with_fake, a, b) == expected
    assert merge_and_list(merge_without_fake, a, b) == expected


def test_simple_example():
    a = [1, 2, 4]
    b = [1, 3, 4]
    expected = [1, 1, 2, 3, 4, 4]
    assert merge_and_list(merge_with_fake, a, b) == expected
    assert merge_and_list(merge_without_fake, a, b) == expected


def test_all_from_one_list():
    a = [1, 2, 3]
    b = [4, 5, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert merge_and_list(merge_with_fake, a, b) == expected
    assert merge_and_list(merge_without_fake, a, b) == expected


def test_with_duplicates():
    a = [1, 1, 2]
    b = [1, 2, 2]
    expected = sorted(a + b)
    assert merge_and_list(merge_with_fake, a, b) == expected
    assert merge_and_list(merge_without_fake, a, b) == expected


def test_negative_and_positive():
    a = [-3, -1, 2]
    b = [-2, 0, 5]
    expected = sorted(a + b)
    assert merge_and_list(merge_with_fake, a, b) == expected
    assert merge_and_list(merge_without_fake, a, b) == expected


def test_random_sorted_lists():
    random.seed(0)
    for _ in range(100):
        n1 = random.randint(0, 20)
        n2 = random.randint(0, 20)
        a = sorted(random.randint(-100, 100) for _ in range(n1))
        b = sorted(random.randint(-100, 100) for _ in range(n2))
        expected = sorted(a + b)

        result_with_fake = merge_and_list(merge_with_fake, a, b)
        result_without_fake = merge_and_list(merge_without_fake, a, b)

        assert result_with_fake == expected
        assert result_without_fake == expected
        assert result_with_fake == result_without_fake
