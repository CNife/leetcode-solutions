"""
1462. 课程表 IV
https://leetcode.cn/problems/course-schedule-iv
"""
import functools


def check_if_prerequisite(num_courses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
    graph = [set() for _ in range(num_courses)]
    for from_, to in prerequisites:
        graph[from_].add(to)

    @functools.lru_cache(None)
    def query(start: int, end: int) -> bool:
        return start == end or any(next_ == end or query(next_, end) for next_ in graph[start])

    return [query(start, end) for start, end in queries]


if __name__ == "__main__":
    assert check_if_prerequisite(2, [[1, 0]], [[0, 1], [1, 0]]) == [False, True]
    assert check_if_prerequisite(3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]) == [True, True]
