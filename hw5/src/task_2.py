"""Перестановки массива с визуализацией рекурсии."""


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


def permutations(nums: list[int]) -> list[list[int]]:
    result: list[list[int]] = []
    used = [False] * len(nums)
    path: list[int] = []

    @tracer
    def backtrack():
        if len(path) == len(nums):
            result.append(path.copy())
            return
        for i, x in enumerate(nums):
            if not used[i]:
                used[i] = True
                path.append(x)
                backtrack()
                path.pop()
                used[i] = False

    backtrack()
    return result