"""
https://leetcode.cn/problems/count-servers-that-communicate/
1267. 统计参与通信的服务器
"""


def count_servers(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    m_count, n_count = [0] * m, [0] * n
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 1:
                m_count[i] += 1
                n_count[j] += 1

    result = 0
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            if value == 1 and (m_count[i] > 1 or n_count[j] > 1):
                result += 1
    return result


if __name__ == "__main__":
    assert count_servers([[1, 0], [0, 1]]) == 0
    assert count_servers([[1, 0], [1, 1]]) == 3
    assert count_servers([[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]) == 4
    assert count_servers([[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1]]) == 8
