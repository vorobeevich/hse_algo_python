"""Стек и очередь на двусвязном списке."""


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def append(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._len += 1

    def appendleft(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self._len += 1

    def pop(self):
        if self.tail is None:
            raise IndexError("pop from empty list")
        node = self.tail
        self.tail = node.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        self._len -= 1
        return node.value

    def popleft(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self._len -= 1
        return node.value

    def __len__(self):
        return self._len


class Stack:
    def __init__(self):
        self._list = DoublyLinkedList()

    def push(self, value):
        self._list.append(value)

    def pop(self):
        if len(self._list) == 0:
            raise IndexError("pop from empty stack")
        return self._list.pop()

    def is_empty(self):
        return len(self._list) == 0

    def __len__(self):
        return len(self._list)


class Queue:
    def __init__(self):
        self._list = DoublyLinkedList()

    def push(self, value):
        self._list.append(value)

    def pop(self):
        if len(self._list) == 0:
            raise IndexError("pop from empty queue")
        return self._list.popleft()

    def is_empty(self):
        return len(self._list) == 0

    def __len__(self):
        return len(self._list)
