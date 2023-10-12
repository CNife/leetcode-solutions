"""
2562. 找出数组的串联值
https://leetcode.cn/problems/find-the-array-concatenation-value
"""


def find_the_array_concatenation_value(nums: list[int]) -> int:
    def concat_nums(a: int, b: int) -> int:
        for bound in [10, 100, 1000, 10000]:
            if b < bound:
                return a * bound + b
        raise ValueError("invalid input")

    result = 0
    for a, b in zip(nums[: len(nums) // 2], reversed(nums)):
        result += concat_nums(a, b)
    if len(nums) % 2 == 1:
        result += nums[len(nums) // 2]
    return result


if __name__ == "__main__":
    assert find_the_array_concatenation_value([7, 52, 2, 4]) == 596
    assert find_the_array_concatenation_value([5, 14, 13, 8, 12]) == 673
