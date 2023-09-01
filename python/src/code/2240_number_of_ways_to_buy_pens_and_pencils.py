"""
2240. 买钢笔和铅笔的方案数
https://leetcode.cn/problems/number-of-ways-to-buy-pens-and-pencils/
"""


def ways_to_buy_pen_pencils(total: int, pen_cost: int, pencil_cost: int) -> int:
    # result = 0
    # for pen_count in range(total // pen_cost + 1):
    #     pencil_total = total - pen_cost * pen_count
    #     pencil_count = pencil_total // pencil_cost + 1
    #     result += pencil_count
    # return result
    return sum((total - pen_cost * pen_count) // pencil_cost + 1 for pen_count in range(total // pen_cost + 1))


if __name__ == "__main__":
    assert ways_to_buy_pen_pencils(20, 10, 5) == 9
    assert ways_to_buy_pen_pencils(5, 10, 10) == 1
