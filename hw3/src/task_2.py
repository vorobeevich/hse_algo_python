"""Группирует слова по анаграммам."""


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}

    for word in words:
        key = "".join(sorted(word))
        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())