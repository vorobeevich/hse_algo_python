"""Слияние двух отсортированных списков двумя способами."""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_with_fake(list1, list2):
    """Слияние с использованием фиктивного узла в начале списка."""
    fake_head = ListNode(0)
    tail = fake_head

    a = list1
    b = list2

    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a is not None:
        tail.next = a
    else:
        tail.next = b

    return fake_head.next


def merge_without_fake(list1, list2):
    """Слияние без фиктивного узла в начале списка."""
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    a = list1
    b = list2

    if a.val <= b.val:
        head = a
        a = a.next
    else:
        head = b
        b = b.next

    tail = head

    while a is not None and b is not None:
        if a.val <= b.val:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    if a is not None:
        tail.next = a
    else:
        tail.next = b

    return head