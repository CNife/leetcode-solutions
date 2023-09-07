"""
1123. 最深叶节点的最近公共祖先
https://leetcode.cn/problems/lowest-common-ancestor-of-deepest-leaves
"""

from leetcode.tree import TreeNode, new_tree


def lca_deepest_leaves(root: TreeNode | None) -> TreeNode | None:
    def search(node: TreeNode | None) -> tuple[TreeNode | None, int]:
        left, left_depth = search(node.left) if node.left else (None, 0)
        right, right_depth = search(node.right) if node.right else (None, 0)
        if left_depth == right_depth:
            return node, left_depth + 1
        if left_depth > right_depth:
            return left, left_depth + 1
        return right, right_depth + 1

    return search(root)[0] if root else None


if __name__ == "__main__":
    t1 = new_tree(3, 5, 1, 6, 2, 0, 8, None, None, 7, 4)
    assert lca_deepest_leaves(t1) is t1.get_node(2)
    t2 = new_tree(1)
    assert lca_deepest_leaves(t2) is t2
    t3 = new_tree(0, 1, 3, None, 2)
    assert lca_deepest_leaves(t3) is t3.get_node(2)
