"""Проверка цикла и топосорт в ориентированном графе."""

def analyze_dag(graph: dict[int, list[int]]) -> tuple[bool, list[int]]:
    vertices = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)

    color = {v: 0 for v in vertices}
    parent = {}
    cycle = None
    order = []

    def dfs(v: int) -> None:
        nonlocal cycle
        color[v] = 1
        for u in graph.get(v, []):
            if color[u] == 0:
                parent[u] = v
                dfs(u)
                if cycle is not None:
                    return
            elif color[u] == 1 and cycle is None:
                path = [u]
                cur = v
                while cur != u:
                    path.append(cur)
                    cur = parent[cur]
                path.append(u)
                path.reverse()
                cycle = path
                return
        color[v] = 2
        order.append(v)

    for v in sorted(vertices):
        if color[v] == 0:
            dfs(v)
            if cycle is not None:
                return True, cycle

    order.reverse()
    return False, order