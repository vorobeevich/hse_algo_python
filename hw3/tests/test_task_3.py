"""Короткие тесты для HashTable."""

import random

import pytest

from src.task_3 import HashTable


def test_put_and_get():
    table = HashTable()
    ref = {}

    table.put("a", 1)
    ref["a"] = 1

    table.put("b", 2)
    ref["b"] = 2

    assert len(table) == len(ref)
    assert table.get("a") == ref["a"]
    assert table.get("b") == ref["b"]


def test_update_value():
    table = HashTable()
    ref = {}

    table.put("x", 1)
    ref["x"] = 1

    table.put("x", 5)
    ref["x"] = 5

    assert len(table) == len(ref)
    assert table.get("x") == ref["x"]


def test_get_and_delete_missing():
    table = HashTable()
    table.put("a", 1)

    with pytest.raises(KeyError):
        table.get("missing")

    with pytest.raises(KeyError):
        table.delete("missing")


def test_delete():
    table = HashTable()
    ref = {}

    for k, v in [("a", 1), ("b", 2), ("c", 3)]:
        table.put(k, v)
        ref[k] = v

    val_t = table.delete("b")
    val_r = ref.pop("b")

    assert val_t == val_r
    assert len(table) == len(ref)
    assert table.get("a") == ref["a"]
    assert table.get("c") == ref["c"]
    with pytest.raises(KeyError):
        table.get("b")


def test_random_operations_against_dict():
    table = HashTable()
    ref = {}

    random.seed(0)
    keys = [f"k{i}" for i in range(20)]

    for _ in range(300):
        op = random.choice(["put", "get", "delete"])
        key = random.choice(keys)

        if op == "put":
            value = random.randint(-100, 100)
            table.put(key, value)
            ref[key] = value

        elif op == "get":
            if key in ref:
                assert table.get(key) == ref[key]
            else:
                with pytest.raises(KeyError):
                    table.get(key)

        else:  # delete
            if key in ref:
                vt = table.delete(key)
                vr = ref.pop(key)
                assert vt == vr
            else:
                with pytest.raises(KeyError):
                    table.delete(key)

    assert len(table) == len(ref)
    for k, v in ref.items():
        assert table.get(k) == v