"""
1466. 重新规划路线
https://leetcode.cn/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero
"""
from collections import defaultdict


def min_reorder(n: int, connections: list[list[int]]) -> int:
    from_connections, to_connections = defaultdict(list), defaultdict(list)
    for from_, to in connections:
        from_connections[from_].append(to)
        to_connections[to].append(from_)

    result, visited = 0, [False] * n

    def dfs(node: int) -> None:
        nonlocal result, visited, from_connections, to_connections

        visited[node] = True
        for next_node in to_connections[node]:
            if not visited[next_node]:
                dfs(next_node)
        for next_node in from_connections[node]:
            if not visited[next_node]:
                result += 1
                dfs(next_node)

    dfs(0)
    return result


if __name__ == "__main__":
    assert min_reorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]) == 3
    assert min_reorder(5, [[1, 0], [1, 2], [3, 2], [3, 4]]) == 2
    assert min_reorder(3, [[1, 0], [2, 0]]) == 0
