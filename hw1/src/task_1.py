"""Проверяет, является ли число палиндромом без использования строк. Разворачиваем число и сравниваем с исходным."""


def is_palindrome(n: int) -> bool:
    if n % 10 == 0:
        return False

    original = n
    reversed_n = 0

    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10

    return original == reversed_n