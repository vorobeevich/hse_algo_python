# hw5/src/task_3.py

"""Простое AVL-дерево с операциями вставки, удаления и поиска.

Дерево хранит только уникальные значения: повторная вставка того же
значения ничего не меняет.
"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def _height(self, node):
        if node is None:
            return 0
        return node.height

    def _update_height(self, node):
        node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, y):
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        self._update_height(x)
        self._update_height(y)
        return y

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)

        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def insert(self, value: int):
        def insert_node(node, value):
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = insert_node(node.left, value)
            elif value > node.value:
                node.right = insert_node(node.right, value)
            else:
                return node  # дубликат, ничего не меняем

            return self._rebalance(node)

        self.root = insert_node(self.root, value)

    def delete(self, value: int):
        def min_node(node):
            while node.left is not None:
                node = node.left
            return node

        def delete_node(node, value):
            if node is None:
                return None

            if value < node.value:
                node.left = delete_node(node.left, value)
            elif value > node.value:
                node.right = delete_node(node.right, value)
            else:
                if node.left is None and node.right is None:
                    return None
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left

                succ = min_node(node.right)
                node.value = succ.value
                node.right = delete_node(node.right, succ.value)

            return self._rebalance(node) if node is not None else None

        self.root = delete_node(self.root, value)

    def find(self, value: int) -> bool:
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False
