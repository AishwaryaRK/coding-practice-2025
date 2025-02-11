from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder_traversal(current, c):
            ans = 0
            if current.left:
                c, ans = inorder_traversal(current.left, c)
            if c == k:
                return c, ans
            c += 1
            if (c == k):
                return c, current.val
            if current.right:
                c, ans = inorder_traversal(current.right, c)
            return c, ans

        _, ans = inorder_traversal(root, 0)
        return ans
