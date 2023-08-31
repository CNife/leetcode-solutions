"""
1761. 一个图中连通三元组的最小度数
https://leetcode.cn/problems/minimum-degree-of-a-connected-trio-in-a-graph
"""
import math
from collections import defaultdict


def min_trio_degree(n: int, edges: list[list[int]]) -> int:
    graph = defaultdict(set)
    degrees = [0] * (n + 1)
    for lhs, rhs in edges:
        if lhs > rhs:
            graph[lhs].add(rhs)
        else:
            graph[rhs].add(lhs)
        degrees[lhs] += 1
        degrees[rhs] += 1

    result = math.inf
    for i in range(n + 1):
        if len(graph[i]) < 2:
            continue
        for j in graph[i]:
            degree = degrees[i] + degrees[j] - 6
            if degree + 2 >= result:
                continue
            for k in graph[i] & graph[j]:
                result = min(result, degrees[k] + degree)

    return result if result != math.inf else -1


if __name__ == "__main__":
    assert min_trio_degree(6, [[1, 2], [1, 3], [3, 2], [4, 1], [5, 2], [3, 6]]) == 3
    assert min_trio_degree(7, [[1, 3], [4, 1], [4, 3], [2, 5], [5, 6], [6, 7], [7, 5], [2, 6]]) == 0
