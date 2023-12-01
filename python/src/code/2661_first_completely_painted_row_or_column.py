"""
2661. 找出叠涂元素
https://leetcode.cn/problems/first-completely-painted-row-or-column
"""


def first_complete_index(arr: list[int], mat: list[list[int]]) -> int:
    # 哈希表
    # m, n = len(mat), len(mat[0])
    # x_counts, y_counts = [0] * m, [0] * n
    # num_2_index = {num: (x, y) for x, line in enumerate(mat) for y, num in enumerate(line)}
    # for i, num in enumerate(arr):
    #     x, y = num_2_index[num]
    #     x_counts[x] += 1
    #     y_counts[y] += 1
    #     if x_counts[x] == n or y_counts[y] == m:
    #         return i
    # raise RuntimeError("unreachable")

    # 不用哈希表
    m, n = len(mat), len(mat[0])
    x_counts, y_counts = [0] * m, [0] * n

    indexes = [0] * m * n * 2
    for x, line in enumerate(mat):
        for y, num in enumerate(line):
            indexes[num * 2 - 2] = x
            indexes[num * 2 - 1] = y

    for i, num in enumerate(arr):
        x, y = indexes[num * 2 - 2], indexes[num * 2 - 1]
        x_counts[x] += 1
        y_counts[y] += 1
        if x_counts[x] == n or y_counts[y] == m:
            return i
    raise RuntimeError("unreachable")


if __name__ == "__main__":
    assert first_complete_index([1, 3, 4, 2], [[1, 4], [2, 3]]) == 2
    assert first_complete_index([2, 8, 7, 4, 1, 3, 5, 6, 9], [[3, 2, 5], [1, 4, 6], [8, 7, 9]]) == 3
    assert first_complete_index([1, 4, 5, 2, 6, 3], [[4, 3, 5], [1, 2, 6]]) == 1
