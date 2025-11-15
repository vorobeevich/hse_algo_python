# hw4/src/task_3.py

"""Проверяет, сбалансировано ли бинарное дерево по высоте."""

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def is_balanced(root) -> bool:
    def height(node):
        if node is None:
            return 0

        left_h = height(node.left)
        if left_h == -1:
            return -1

        right_h = height(node.right)
        if right_h == -1:
            return -1

        if abs(left_h - right_h) > 1:
            return -1

        return max(left_h, right_h) + 1

    return height(root) != -1
