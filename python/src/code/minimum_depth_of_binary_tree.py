from leetcode.tree import TreeNode, new_tree


def min_depth(root: TreeNode) -> int:
    if not root:
        return 0

    def inner(node: TreeNode) -> int:
        if node.left and node.right:
            return min(inner(node.left), inner(node.right)) + 1
        if node.left:
            return inner(node.left) + 1
        if node.right:
            return inner(node.right) + 1
        return 1

    return inner(root)


if __name__ == "__main__":
    assert min_depth(new_tree(3, 9, 20, None, None, 15, 7)) == 2
    assert min_depth(new_tree(1, 2)) == 2
