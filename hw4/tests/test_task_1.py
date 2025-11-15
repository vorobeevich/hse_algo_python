"""Тесты для обходов BST."""

from src.task_1 import BST


def build_basic_tree() -> BST:
    tree = BST()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        tree.insert(v)
    return tree


def test_empty_tree_traversals():
    tree = BST()
    assert tree.preorder() == []
    assert tree.inorder() == []
    assert tree.postorder() == []
    assert tree.reverse_preorder() == []
    assert tree.reverse_inorder() == []
    assert tree.reverse_postorder() == []


def test_single_node_traversals():
    tree = BST()
    tree.insert(10)
    expected = [10]
    assert tree.preorder() == expected
    assert tree.inorder() == expected
    assert tree.postorder() == expected
    assert tree.reverse_preorder() == expected
    assert tree.reverse_inorder() == expected
    assert tree.reverse_postorder() == expected


def test_basic_tree_traversals():
    tree = build_basic_tree()

    assert tree.preorder() == [5, 3, 2, 4, 7, 6, 8]
    assert tree.inorder() == [2, 3, 4, 5, 6, 7, 8]
    assert tree.postorder() == [2, 4, 3, 6, 8, 7, 5]

    assert tree.reverse_preorder() == [5, 7, 8, 6, 3, 4, 2]
    assert tree.reverse_inorder() == [8, 7, 6, 5, 4, 3, 2]
    assert tree.reverse_postorder() == [8, 6, 7, 4, 2, 3, 5]


def test_inorder_with_duplicates():
    tree = BST()
    for v in [5, 5, 5, 5]:
        tree.insert(v)

    assert tree.inorder() == [5, 5, 5, 5]


def test_skewed_tree_traversals():
    tree = BST()
    for v in [1, 2, 3, 4]:
        tree.insert(v)

    assert tree.preorder() == [1, 2, 3, 4]
    assert tree.inorder() == [1, 2, 3, 4]
    assert tree.postorder() == [4, 3, 2, 1]

    assert tree.reverse_preorder() == [1, 2, 3, 4]
    assert tree.reverse_inorder() == [4, 3, 2, 1]
    assert tree.reverse_postorder() == [4, 3, 2, 1]