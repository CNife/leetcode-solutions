"""
1921. 消灭怪物的最大数量
https://leetcode.cn/problems/eliminate-maximum-number-of-monsters/
"""


def eliminate_maximum(distances: list[int], speeds: list[int]) -> int:
    arrive_times = [distance / speed for distance, speed in zip(distances, speeds)]
    arrive_times.sort()
    for i, arrive_time in enumerate(arrive_times):
        if i >= arrive_time:
            return i
    return len(arrive_times)


if __name__ == "__main__":
    assert eliminate_maximum([1, 3, 4], [1, 1, 1]) == 3
    assert eliminate_maximum([1, 1, 2, 3], [1, 1, 1, 1]) == 1
    assert eliminate_maximum([3, 2, 4], [5, 3, 2]) == 1
