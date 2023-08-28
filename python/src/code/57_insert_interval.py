"""
57. 插入区间
https://leetcode.cn/problems/insert-interval/
"""

from typing import TypeAlias

Interval: TypeAlias = list[int]


def insert(intervals: list[Interval], new_interval: Interval) -> list[Interval]:
    result = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    while i < n and (intervals[i][1] >= new_interval[0] and intervals[i][0] <= new_interval[1]):
        new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
        i += 1
    result.append(new_interval)
    while i < n:
        result.append(intervals[i])
        i += 1
    return result


if __name__ == "__main__":
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert insert([], [5, 7]) == [[5, 7]]
    assert insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert insert([[1, 5]], [2, 7]) == [[1, 7]]
