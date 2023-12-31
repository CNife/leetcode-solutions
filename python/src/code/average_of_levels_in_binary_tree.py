from collections import deque
from itertools import zip_longest
from math import isclose

from leetcode.tree import TreeNode, new_tree


def average_of_levels(root: TreeNode) -> list[float]:
    if not root:
        return []

    queue = deque()
    queue.append(root)
    result = []

    while queue:
        level_length = len(queue)
        level_sum = 0
        for _ in range(level_length):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_sum / level_length)
    return result


if __name__ == "__main__":
    tests = [(new_tree(3, 9, 20, None, None, 15, 7), [3, 14.5, 11])]
    for tree, want in tests:
        assert all(isclose(lhs, rhs) for lhs, rhs in zip_longest(average_of_levels(tree), want, fillvalue=float("NaN")))
