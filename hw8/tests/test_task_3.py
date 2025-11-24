"""Тесты для поиска цикла и топосортировки в ориентированном графе."""

import random

import networkx as nx

from src.task_3 import analyze_dag


def is_valid_topo(graph: dict[int, list[int]], order: list[int]) -> bool:
    pos = {v: i for i, v in enumerate(order)}
    for v, neighbors in graph.items():
        for u in neighbors:
            if pos[v] >= pos[u]:
                return False
    return True


def is_valid_cycle(graph: dict[int, list[int]], cycle: list[int]) -> bool:
    if len(cycle) < 2 or cycle[0] != cycle[-1]:
        return False
    seen = set(cycle[:-1])
    if len(seen) != len(cycle) - 1:
        return False
    for a, b in zip(cycle, cycle[1:]):
        if b not in graph.get(a, []):
            return False
    return True


def test_empty_graph():
    graph = {}
    has_cycle, result = analyze_dag(graph)
    assert not has_cycle
    assert result == []


def test_single_vertex_no_edges():
    graph = {0: []}
    has_cycle, result = analyze_dag(graph)
    assert not has_cycle
    assert result == [0]


def test_multiple_isolated_vertices():
    graph = {0: [], 1: [], 2: []}
    has_cycle, result = analyze_dag(graph)
    assert not has_cycle
    assert sorted(result) == [0, 1, 2]
    assert is_valid_topo(graph, result)


def test_simple_dag_chain():
    graph = {
        1: [2],
        2: [3],
        3: [],
    }
    has_cycle, result = analyze_dag(graph)
    assert not has_cycle
    assert is_valid_topo(graph, result)
    assert sorted(result) == [1, 2, 3]


def test_simple_cycle():
    graph = {
        1: [2],
        2: [3],
        3: [1],
    }
    has_cycle, result = analyze_dag(graph)
    assert has_cycle
    assert is_valid_cycle(graph, result)


def test_tail_into_cycle():
    graph = {
        1: [2],
        2: [3],
        3: [4],
        4: [2],
    }
    has_cycle, result = analyze_dag(graph)
    assert has_cycle
    assert is_valid_cycle(graph, result)


def test_mixed_components():
    graph = {
        1: [2],
        2: [],
        3: [4],
        4: [3],
        5: [],
    }
    has_cycle, result = analyze_dag(graph)
    assert has_cycle
    assert is_valid_cycle(graph, result)


def test_random_graph_against_networkx():
    random.seed(0)
    n = 12
    p = 0.2

    g_nx = nx.gnp_random_graph(n, p, directed=True)
    graph = {v: [] for v in g_nx.nodes()}
    for u, v in g_nx.edges():
        graph[u].append(v)

    has_cycle, result = analyze_dag(graph)
    is_dag = nx.is_directed_acyclic_graph(g_nx)

    assert has_cycle == (not is_dag)

    if not has_cycle:
        assert sorted(result) == sorted(graph.keys())
        assert is_valid_topo(graph, result)