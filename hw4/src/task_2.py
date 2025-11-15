"""Проверяет, является ли дерево бинарным деревом поиска (BST)."""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if self.root is None:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = Node(value)
                    return
                node = node.right


def validate_bst(root) -> bool:
    """Проверяет, что дерево удовлетворяет правилу: слева <, справа >=."""

    def check(node, low, high):
        if node is None:
            return True
        if not (low <= node.value < high):
            return False
        return check(node.left, low, node.value) and check(node.right, node.value, high)

    return check(root, float("-inf"), float("inf"))