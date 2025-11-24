"""Тесты для алгоритма Дейкстры."""

import random

import networkx as nx

from src.task_2 import dijkstra


def test_single_vertex_no_edges():
    graph = {0: []}
    dist = dijkstra(graph, 0)
    assert dist == {0: 0}


def test_simple_chain_undirected():
    graph = {
        0: [(1, 1)],
        1: [(0, 1), (2, 2)],
        2: [(1, 2)],
    }
    dist = dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[1] == 1
    assert dist[2] == 3


def test_disconnected_graph():
    graph = {
        0: [(1, 5)],
        1: [(0, 5)],
        2: [],
    }
    dist = dijkstra(graph, 0)
    assert dist == {0: 0, 1: 5}
    assert 2 not in dist


def test_cycle_with_better_indirect_path():
    graph = {
        0: [(1, 10), (2, 1)],
        1: [(0, 10), (2, 1)],
        2: [(0, 1), (1, 1)],
    }
    dist = dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[2] == 1
    assert dist[1] == 2 


def test_zero_weight_edges():
    graph = {
        0: [(1, 0), (2, 5)],
        1: [(0, 0), (2, 1)],
        2: [(0, 5), (1, 1)],
    }
    dist = dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[1] == 0
    assert dist[2] == 1


def test_random_graph_against_networkx():
    random.seed(0)
    n = 15
    p = 0.3

    g_nx = nx.gnp_random_graph(n, p, directed=False)

    graph = {i: [] for i in range(n)}
    for u, v in g_nx.edges():
        w = random.randint(1, 10)
        graph[u].append((v, w))
        graph[v].append((u, w))
        g_nx[u][v]["weight"] = w

    source = 0
    dist_ours = dijkstra(graph, source)
    dist_nx = nx.single_source_dijkstra_path_length(g_nx, source, weight="weight")

    assert dist_ours == dist_nx