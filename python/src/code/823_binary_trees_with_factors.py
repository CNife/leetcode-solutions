"""
823. 带因子的二叉树
https://leetcode.cn/problems/binary-trees-with-factors/description/
"""
import functools


def num_factored_binary_trees(arr: list[int]) -> int:
    @functools.lru_cache(None)
    def dfs(root: int) -> int:
        result = 1
        for value in arr:
            if root % value == 0 and (root // value) in arr:
                result += dfs(value) * dfs(root // value)
        return result

    return sum(dfs(x) for x in arr) % (10**9 + 7)


if __name__ == "__main__":
    assert num_factored_binary_trees([2, 4]) == 3
    assert num_factored_binary_trees([2, 4, 5, 10]) == 7
