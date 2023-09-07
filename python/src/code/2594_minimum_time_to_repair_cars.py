"""
2594. 修车的最少时间
https://leetcode.cn/problems/minimum-time-to-repair-cars/
"""
from math import floor, sqrt


def repair_cars(ranks: list[int], cars: int) -> int:
    left, right = 1, ranks[0] * cars**2
    while left < right:
        middle = (left + right) // 2
        cars_repaired = sum(floor(sqrt(middle / rank)) for rank in ranks)
        if cars_repaired >= cars:
            right = middle
        else:
            left = middle + 1
    return left


if __name__ == "__main__":
    assert repair_cars([4, 2, 3, 1], 10) == 16
    assert repair_cars([5, 1, 8], 6) == 16
