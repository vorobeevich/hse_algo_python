"""Поиск компонент связности в неориентированном графе."""


def dfs(graph: dict[int, list[int]], v: int, visited: set[int], comp: list[int]) -> None:
    visited.add(v)
    comp.append(v)
    for u in graph.get(v, []):
        if u not in visited:
            dfs(graph, u, visited, comp)


def connected_components(graph: dict[int, list[int]]) -> list[list[int]]:
    visited = set()
    components = []

    for start in sorted(graph.keys()):
        if start in visited:
            continue
        comp = []
        dfs(graph, start, visited, comp)
        comp.sort()
        components.append(comp)

    components.sort(key=lambda c: c[0] if c else 0)
    return components