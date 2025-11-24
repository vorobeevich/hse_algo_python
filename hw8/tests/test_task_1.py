"""Тесты для поиска компонент связности в графе."""

import random
import networkx as nx

from src.task_1 import connected_components


def norm(comps):
    return sorted([sorted(c) for c in comps])


def test_empty_graph():
    graph = {}
    assert norm(connected_components(graph)) == []


def test_single_vertex_no_edges():
    graph = {1: []}
    assert norm(connected_components(graph)) == [[1]]


def test_multiple_isolated_vertices():
    graph = {1: [], 2: [], 3: []}
    assert norm(connected_components(graph)) == [[1], [2], [3]]


def test_single_component_chain():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2],
    }
    assert norm(connected_components(graph)) == [[1, 2, 3]]


def test_multiple_components_and_isolated():
    graph = {
        1: [2],
        2: [1],
        3: [],
        4: [5],
        5: [4],
    }
    expected = [[1, 2], [3], [4, 5]]
    assert norm(connected_components(graph)) == norm(expected)


def test_self_loop_and_duplicates():
    graph = {
        1: [1, 2, 2],
        2: [1, 1],
        3: [3],
    }
    expected = [[1, 2], [3]]
    assert norm(connected_components(graph)) == norm(expected)


def test_neighbor_order_does_not_matter():
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3],
        5: [],
        6: [7],
        7: [6],
    }
    base = norm(connected_components(graph))

    random.seed(0)
    for _ in range(20):
        shuffled = {v: neighbors[:] for v, neighbors in graph.items()}
        for neighbors in shuffled.values():
            random.shuffle(neighbors)
        assert norm(connected_components(shuffled)) == base

def test_random_graph_against_networkx():
    if nx is None:
        return

    random.seed(0)
    n = 15
    graph = {i: [] for i in range(n)}

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < 0.2:
                graph[i].append(j)
                graph[j].append(i)

    ours = norm(connected_components(graph))

    g = nx.Graph()
    g.add_nodes_from(range(n))
    for v, neighbors in graph.items():
        for u in neighbors:
            g.add_edge(v, u)

    expected = norm([list(c) for c in nx.connected_components(g)])

    assert ours == expected
