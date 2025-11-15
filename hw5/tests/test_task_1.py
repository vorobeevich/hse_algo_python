"""Тесты для декоратора tracer."""

from src.task_1 import tracer


@tracer
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)


@tracer
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def test_tracer_factorial(capsys):
    result = fact(3)
    out = capsys.readouterr().out.strip().splitlines()

    assert result == 6
    assert out == [
        "fact(3)",
        "  fact(2)",
        "    fact(1)",
        "    return 1",
        "  return 2",
        "return 6",
    ]


def test_tracer_fib(capsys):
    result = fib(2)
    out = capsys.readouterr().out.strip().splitlines()

    assert result == 1
    assert out == [
        "fib(2)",
        "  fib(1)",
        "  return 1",
        "  fib(0)",
        "  return 0",
        "return 1",
    ]