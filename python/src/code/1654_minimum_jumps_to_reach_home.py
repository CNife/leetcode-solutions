"""
1654. 到家的最少跳跃次数
https://leetcode.cn/problems/minimum-jumps-to-reach-home/
"""
from collections import deque


def minimum_jumps(forbidden: list[int], right_hop: int, left_hop: int, target: int) -> int:
    forbidden = set(forbidden)
    queue, visited = deque[tuple[int, int, int]]([(0, 1, 0)]), {0}
    bound = max(max(forbidden) + right_hop, target) + left_hop
    while queue:
        position, direction, steps = queue.popleft()
        if position == target:
            return steps
        if (
            0 <= (next_position := position + right_hop) <= bound
            and next_position not in visited
            and next_position not in forbidden
        ):
            visited.add(next_position)
            queue.append((next_position, 1, steps + 1))
        if (
            direction == 1
            and 0 <= (next_position := position - left_hop) <= bound
            and -next_position not in visited
            and next_position not in forbidden
        ):
            visited.add(-next_position)
            queue.append((next_position, -1, steps + 1))
    return -1


if __name__ == "__main__":
    assert minimum_jumps([14, 4, 18, 1, 15], 3, 15, 9) == 3
    assert minimum_jumps([8, 3, 16, 6, 12, 20], 15, 13, 11) == -1
    assert minimum_jumps([1, 6, 2, 14, 5, 17, 4], 16, 9, 7) == 2
