"""Проверяет, может ли пара последовательностей быть результатом работы стека."""


def validate_stack_sequences(pushed: list[int], popped: list[int]) -> bool:
    if len(pushed) != len(popped):
        return False

    stack: list[int] = []
    i = 0
    n = len(pushed)

    for x in popped:
        while (not stack or stack[-1] != x) and i < n:
            stack.append(pushed[i])
            i += 1

        if not stack or stack[-1] != x:
            return False

        stack.pop()

    return True
