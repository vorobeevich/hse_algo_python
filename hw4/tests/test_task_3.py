"""Тесты для is_balanced."""

from src.task_3 import Node, is_balanced


def test_empty_tree():
    assert is_balanced(None)


def test_single_node():
    root = Node(1)
    assert is_balanced(root)


def test_perfect_balanced_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    assert is_balanced(root)


def test_balanced_but_not_perfect():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    assert is_balanced(root)


def test_simple_unbalanced():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(3)

    assert not is_balanced(root)


def test_unbalanced_deep_left():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)

    assert not is_balanced(root)


def test_unbalanced_deep_right():
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)

    assert not is_balanced(root)


def test_subtree_unbalanced_while_root_seems_ok():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.left.left = Node(5)

    assert not is_balanced(root)


def test_leaf_difference_one_is_ok():
    root = Node(1)
    root.left = Node(2)

    assert is_balanced(root)