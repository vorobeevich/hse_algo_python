"""Тесты для group_anagrams."""

import random

from src.task_2 import group_anagrams


def normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


def test_empty_list():
    assert group_anagrams([]) == []


def test_single_word():
    result = group_anagrams(["abc"])
    assert normalize(result) == [["abc"]]


def test_example_from_statement():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(words)
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert normalize(result) == normalize(expected)


def test_no_anagrams_all_separate():
    words = ["abc", "def", "ghi"]
    result = group_anagrams(words)
    expected = [["abc"], ["def"], ["ghi"]]
    assert normalize(result) == normalize(expected)


def test_all_in_one_group():
    words = ["ab", "ba", "a b".replace(" ", ""), "b a".replace(" ", "")]
    result = group_anagrams(words)
    expected = [["ab", "ba", "ab", "ba"]]
    assert normalize(result) == normalize(expected)


def test_with_duplicates():
    words = ["eat", "tea", "tea", "ate"]
    result = group_anagrams(words)
    expected = [["eat", "tea", "tea", "ate"]]
    assert normalize(result) == normalize(expected)


def test_single_letter_words():
    words = ["a", "b", "a", "c", "b"]
    result = group_anagrams(words)
    expected = [["a", "a"], ["b", "b"], ["c"]]
    assert normalize(result) == normalize(expected)


def test_random_shuffles_same_groups():
    base = ["eat", "tea", "tan", "ate", "nat", "bat", "foo", "oof", "bar", "arb", "zzz"]
    expected = normalize(group_anagrams(base))

    random.seed(0)
    for _ in range(100):
        words = base[:]
        random.shuffle(words)
        result = group_anagrams(words)
        assert normalize(result) == expected