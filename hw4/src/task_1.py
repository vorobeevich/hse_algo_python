"""BST с разными обходами."""

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

    def preorder(self) -> list[int]:
        def visit(node, acc):
            if node is None:
                return
            acc.append(node.value)
            visit(node.left, acc)
            visit(node.right, acc)

        result: list[int] = []
        visit(self.root, result)
        return result

    def inorder(self) -> list[int]:
        def visit(node, acc):
            if node is None:
                return
            visit(node.left, acc)
            acc.append(node.value)
            visit(node.right, acc)

        result: list[int] = []
        visit(self.root, result)
        return result

    def postorder(self) -> list[int]:
        def visit(node, acc):
            if node is None:
                return
            visit(node.left, acc)
            visit(node.right, acc)
            acc.append(node.value)

        result: list[int] = []
        visit(self.root, result)
        return result

    def reverse_preorder(self) -> list[int]:
        def visit(node, acc):
            if node is None:
                return
            acc.append(node.value)
            visit(node.right, acc)
            visit(node.left, acc)

        result: list[int] = []
        visit(self.root, result)
        return result

    def reverse_inorder(self) -> list[int]:
        def visit(node, acc):
            if node is None:
                return
            visit(node.right, acc)
            acc.append(node.value)
            visit(node.left, acc)

        result: list[int] = []
        visit(self.root, result)
        return result

    def reverse_postorder(self) -> list[int]:
        def visit(node, acc):
            if node is None:
                return
            visit(node.right, acc)
            visit(node.left, acc)
            acc.append(node.value)

        result: list[int] = []
        visit(self.root, result)
        return result