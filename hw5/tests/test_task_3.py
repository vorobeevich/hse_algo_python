# hw5/tests/test_task_3.py

"""Тесты для AVL-дерева."""

import random

from src.task_3 import AVL


def inorder_values(node):
    if node is None:
        return []
    return inorder_values(node.left) + [node.value] + inorder_values(node.right)


def is_bst(node, low, high):
    if node is None:
        return True
    if not (low < node.value < high):
        return False
    return is_bst(node.left, low, node.value) and is_bst(node.right, node.value, high)


def check_balanced(node):
    if node is None:
        return 0
    left_h = check_balanced(node.left)
    right_h = check_balanced(node.right)
    assert abs(left_h - right_h) <= 1
    return max(left_h, right_h) + 1


def assert_avl(root):
    assert is_bst(root, float("-inf"), float("inf"))
    check_balanced(root)


def test_empty_tree():
    tree = AVL()
    assert not tree.find(10)
    assert_avl(tree.root)


def test_insert_and_find_basic():
    tree = AVL()
    values = [10, 20, 30, 40, 50, 25]

    for v in values:
        tree.insert(v)

    for v in values:
        assert tree.find(v)

    assert not tree.find(100)
    assert inorder_values(tree.root) == sorted(values)
    assert_avl(tree.root)


def test_insert_duplicates_ignored():
    tree = AVL()
    tree.insert(10)
    tree.insert(10)
    tree.insert(10)

    assert tree.find(10)
    assert inorder_values(tree.root) == [10]
    assert_avl(tree.root)


def test_delete_leaf():
    tree = AVL()
    for v in [20, 10, 30]:
        tree.insert(v)

    tree.delete(10)
    assert not tree.find(10)
    assert inorder_values(tree.root) == [20, 30]
    assert_avl(tree.root)


def test_delete_node_with_one_child():
    tree = AVL()
    for v in [20, 10, 5]:
        tree.insert(v)

    tree.delete(10)
    assert not tree.find(10)
    assert inorder_values(tree.root) == sorted([20, 5])
    assert_avl(tree.root)


def test_delete_node_with_two_children():
    tree = AVL()
    for v in [30, 20, 40, 10, 25, 35, 50]:
        tree.insert(v)

    tree.delete(20)
    assert not tree.find(20)

    expected = [30, 40, 10, 25, 35, 50]
    assert inorder_values(tree.root) == sorted(expected)
    assert_avl(tree.root)


def test_delete_root_until_empty():
    tree = AVL()
    values = [10, 5, 15, 3, 7, 12, 18]
    for v in values:
        tree.insert(v)

    for v in values:
        tree.delete(v)
        assert not tree.find(v)
        assert_avl(tree.root)

    assert tree.root is None


def test_random_insert_delete():
    random.seed(0)
    tree = AVL()
    values = list(range(30))
    random.shuffle(values)

    for v in values:
        tree.insert(v)
    assert_avl(tree.root)

    random.shuffle(values)
    removed = set()

    for v in values[:20]:
        tree.delete(v)
        removed.add(v)
        assert not tree.find(v)
        assert_avl(tree.root)

    for v in values[20:]:
        assert tree.find(v)

    remaining = sorted(set(values) - removed)
    assert inorder_values(tree.root) == remaining
    assert_avl(tree.root)
