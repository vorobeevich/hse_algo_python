"""Тесты для validate_bst."""

from src.task_2 import BST, Node, validate_bst


def test_empty_tree_is_valid():
    assert validate_bst(None)


def test_single_node_is_valid():
    tree = BST()
    tree.insert(10)
    assert validate_bst(tree.root)


def test_valid_bst_simple():
    tree = BST()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(v)
    assert validate_bst(tree.root)


def test_valid_bst_with_duplicates_on_right():
    tree = BST()
    for v in [5, 5, 5, 5]:
        tree.insert(v)
    assert validate_bst(tree.root)


def test_invalid_bst_left_child_equal_to_parent():
    root = Node(5)
    root.left = Node(5)
    assert not validate_bst(root)


def test_invalid_bst_right_child_less_than_parent():
    root = Node(5)#
    root.right = Node(4)
    assert not validate_bst(root)


def test_invalid_bst_violation_deep_left():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.right = Node(12)
    assert not validate_bst(root)


def test_invalid_bst_violation_deep_right():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(3)
    assert not validate_bst(root)


def test_right_chain_valid():
    tree = BST()
    for v in [1, 2, 3, 4]:
        tree.insert(v)
    assert validate_bst(tree.root)


def test_left_chain_valid():
    tree = BST()
    for v in [4, 3, 2, 1]:
        tree.insert(v)
    assert validate_bst(tree.root)