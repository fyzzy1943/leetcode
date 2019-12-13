# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return None

        if root.left is None and root.right is None:
            if root.val < limit:
                return None
            return root

        left = self.sufficientSubset(root.left, limit - root.val)
        right = self.sufficientSubset(root.right, limit - root.val)

        if left is None and right is None:
            return None

        root.left = left
        root.right = right
        return root
