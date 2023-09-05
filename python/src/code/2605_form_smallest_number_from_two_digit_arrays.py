"""
2605. 从两个数字数组里生成最小数字
https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays/
"""


def min_number(nums1: list[int], nums2: list[int]) -> int:
    nums1, nums2 = set(nums1), set(nums2)
    if same_digits := nums1 & nums2:
        return min(same_digits)

    min1, min2 = min(nums1), min(nums2)
    return min(min1, min2) * 10 + max(min1, min2)


if __name__ == "__main__":
    assert min_number([4, 1, 3], [5, 7]) == 15
    assert min_number([3, 5, 2, 6], [3, 1, 7]) == 3
