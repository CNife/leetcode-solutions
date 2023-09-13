"""
2596. 检查骑士巡视方案
https://leetcode.cn/problems/check-knight-tour-configuration/
"""


def check_valid_grid(grid: list[list[int]]) -> bool:
    if grid[0][0] != 0:
        return False

    indexes: list[tuple[int, int]] = [(-1, -1)] * len(grid) * len(grid[0])
    for i, row in enumerate(grid):
        for j, value in enumerate(row):
            indexes[value] = (i, j)

    prev_x, prev_y = indexes[0]
    for x, y in indexes[1:]:
        x_diff, y_diff = abs(prev_x - x), abs(prev_y - y)
        if x_diff == 1 and y_diff == 2 or x_diff == 2 and y_diff == 1:
            prev_x, prev_y = x, y
        else:
            return False
    return True


if __name__ == "__main__":
    assert (
        check_valid_grid(
            [[0, 11, 16, 5, 20], [17, 4, 19, 10, 15], [12, 1, 8, 21, 6], [3, 18, 23, 14, 9], [24, 13, 2, 7, 22]]
        )
        is True
    )
    assert check_valid_grid([[0, 3, 6], [5, 8, 1], [2, 7, 4]]) is False
    assert (
        check_valid_grid(
            [[24, 11, 22, 17, 4], [21, 16, 5, 12, 9], [6, 23, 10, 3, 18], [15, 20, 1, 8, 13], [0, 7, 14, 19, 2]]
        )
        is False
    )
