"""
56. 合并区间
https://leetcode.cn/problems/merge-intervals/description/
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    result = []
    for start, end in sorted(intervals, key=lambda interval: interval[0]):
        if result and result[-1][1] >= start:
            result[-1][1] = max(end, result[-1][1])
        else:
            result.append([start, end])
    return result


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [0, 1]]) == [[0, 4]]
    assert merge([[1, 4], [0, 0]]) == [[0, 0], [1, 4]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]
