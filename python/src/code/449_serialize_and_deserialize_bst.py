"""
449. 序列化和反序列化二叉搜索树
https://leetcode.cn/problems/serialize-and-deserialize-bst/
"""
# import base64
# import pickle
#
# from leetcode.tree import TreeNode
#
#
# class Codec:
#     def serialize(self, root: TreeNode | None) -> str:
#         return str(base64.b64encode(pickle.dumps(root)), encoding="UTF-8")
#
#     def deserialize(self, data: str) -> TreeNode | None:
#         return pickle.loads(base64.b64decode(bytes(data, encoding="UTF-8"), validate=True))

from collections import deque

from leetcode.tree import TreeNode


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        queue, values = deque([root]), []
        while queue:
            node = queue.popleft()
            values.append(str(node.val) if node else "")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(values)

    def deserialize(self, data: str) -> TreeNode | None:
        if not data:
            return None
        values = [int(val) if val else None for val in data.split(",")]

        root, node = TreeNode(values[0]), None
        queue = deque([root])
        for value in values[1:]:
            if not node:
                node = queue.popleft()
                if value is not None:
                    node.left = TreeNode(value)
                    queue.append(node.left)
            else:
                if value is not None:
                    node.right = TreeNode(value)
                    queue.append(node.right)
                node = None
        return root


if __name__ == "__main__":
    from leetcode.tree import new_tree

    codec = Codec()
    tree1 = new_tree(2, 1, 3)
    assert codec.deserialize(codec.serialize(tree1)) == tree1
    tree2 = new_tree()
    assert codec.deserialize(codec.serialize(tree2)) == tree2
    tree3 = new_tree(1, None, 2)
    assert codec.deserialize(codec.serialize(tree3)) == tree3
