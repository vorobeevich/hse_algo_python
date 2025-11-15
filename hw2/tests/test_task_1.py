"""Тесты для стека и очереди на двусвязном списке."""

import random
from collections import deque

import pytest

from src.task_1 import Stack, Queue


def test_stack_single_element():
    s = Stack()
    s.push(1)
    assert not s.is_empty()
    assert len(s) == 1
    assert s.pop() == 1
    assert s.is_empty()
    assert len(s) == 0


def test_stack_multiple_elements_lifo():
    s = Stack()
    for x in [1, 2, 3]:
        s.push(x)
    assert s.pop() == 3
    assert s.pop() == 2
    assert s.pop() == 1
    assert s.is_empty()


def test_stack_pop_empty_raises():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()


def test_queue_single_element():
    q = Queue()
    q.push(1)
    assert not q.is_empty()
    assert len(q) == 1
    assert q.pop() == 1
    assert q.is_empty()
    assert len(q) == 0


def test_queue_multiple_elements_fifo():
    q = Queue()
    for x in [1, 2, 3]:
        q.push(x)
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3
    assert q.is_empty()


def test_queue_pop_empty_raises():
    q = Queue()
    with pytest.raises(IndexError):
        q.pop()


def test_stack_random_sequence():
    random.seed(0)
    s = Stack()
    ref = []
    for _ in range(1000):
        if not ref or random.random() < 0.7:
            value = random.randint(-1000, 1000)
            s.push(value)
            ref.append(value)
        else:
            assert s.pop() == ref.pop()
        assert len(s) == len(ref)
        assert s.is_empty() == (len(ref) == 0)


def test_queue_random_sequence():
    random.seed(1)
    q = Queue()
    ref = deque()
    for _ in range(1000):
        if not ref or random.random() < 0.7:
            value = random.randint(-1000, 1000)
            q.push(value)
            ref.append(value)
        else:
            assert q.pop() == ref.popleft()
        assert len(q) == len(ref)
        assert q.is_empty() == (len(ref) == 0)
