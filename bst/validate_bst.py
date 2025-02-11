import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def bst(current, lower_bound, upper_bound):
            if not current:
                return True
            if current.val < lower_bound or current.val > upper_bound:
                return False
            if current.left:
                v1 = bst(current.left, lower_bound, current.val)
                if not v1:
                    return False
            if current.right:
                v2 = bst(current.right, current.val, upper_bound)
                if not v2:
                    return False
            return True

        return bst(root, -math.inf, math.inf)
