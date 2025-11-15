"""Декоратор, который печатает стек вызовов рекурсивной функции.

Пример:

    @tracer
    def fact(n):
        if n <= 1:
            return 1
        return n * fact(n - 1)

    fact(3)

Вывод:

    fact(3)
      fact(2)
        fact(1)
        return 1
      return 2
    return 6
"""


def tracer(func):
    depth = 0

    def wrapper(*args, **kwargs):
        nonlocal depth
        indent = "  " * depth
        args_str = ", ".join(str(a) for a in args)
        print(f"{indent}{func.__name__}({args_str})")
        depth += 1
        result = func(*args, **kwargs)
        depth -= 1
        indent = "  " * depth
        print(f"{indent}return {result}")
        return result

    return wrapper