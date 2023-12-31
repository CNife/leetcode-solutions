import heapq
from collections import defaultdict


# 递归 DFS
def find_itinerary(tickets: list[list[int]]) -> list[str]:
    result = []
    if not tickets:
        return result

    graph = defaultdict(list)
    for pair in tickets:
        start, end = pair[:2]
        heapq.heappush(graph[start], end)

    def visit(src: str) -> None:
        nonlocal result, graph
        nbr = graph[src]
        while nbr:
            dest = heapq.heappop(nbr)
            visit(dest)
        result.append(src)

    visit("JFK")
    result.reverse()
    return result


if __name__ == "__main__":
    assert find_itinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]) == [
        "JFK",
        "MUC",
        "LHR",
        "SFO",
        "SJC",
    ]
    assert find_itinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]) == [
        "JFK",
        "ATL",
        "JFK",
        "SFO",
        "ATL",
        "SFO",
    ]
