"""Алгоритм Дейкстры для взвешенного графа."""

import heapq


def dijkstra(graph: dict[int, list[tuple[int, int]]], start: int) -> dict[int, int]:
    dist = {}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        d, v = heapq.heappop(heap)
        if d != dist.get(v, d):
            continue
        for u, w in graph.get(v, []):
            nd = d + w
            if u not in dist or nd < dist[u]:
                dist[u] = nd
                heapq.heappush(heap, (nd, u))

    return dist