"""
1448. 统计二叉树中好节点的数目
https://leetcode.cn/problems/count-good-nodes-in-binary-tree
"""
from leetcode.tree import TreeNode, new_tree


def good_nodes(root: TreeNode) -> int:
    def find_good_nodes(node: TreeNode, max_value: int) -> int:
        max_value = max(max_value, node.val)
        result = int(node.val >= max_value)
        if node.left is not None:
            result += find_good_nodes(node.left, max_value)
        if node.right is not None:
            result += find_good_nodes(node.right, max_value)
        return result

    return find_good_nodes(root, root.val)


if __name__ == "__main__":
    assert good_nodes(new_tree(3, 1, 4, 3, None, 1, 5)) == 4
    assert good_nodes(new_tree(3, 3, None, 4, 2)) == 3
    assert good_nodes(new_tree(1)) == 1
