"""
2591. 将钱分给最多的儿童
https://leetcode.cn/problems/distribute-money-to-maximum-children
"""


def dist_money(money: int, children: int) -> int:
    if money < children:
        return -1
    all_fulfilled = children * 8
    if money < all_fulfilled:
        valid_count, remaining = (money - children) // 7, (money - children) % 7
        if remaining == 3 and valid_count == children - 1:
            return children - 2
        return valid_count
    if money == all_fulfilled:
        return children
    if money > all_fulfilled:
        return children - 1


if __name__ == "__main__":
    assert dist_money(20, 3) == 1
    assert dist_money(16, 2) == 2
    assert dist_money(3, 1) == 0
    assert dist_money(1, 1) == 0
    assert dist_money(2, 2) == 0
