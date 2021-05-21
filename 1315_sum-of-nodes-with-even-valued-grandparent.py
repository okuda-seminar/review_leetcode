# V = node num
# time: O(V)
# space: O(V)
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        stack = deque([(None, None, root)])
        ret = 0
        while stack:
            gp, p, n = stack.pop()
            if n is None:
                continue
            ret += (gp is not None and gp.val % 2 == 0) * n.val
            stack.append((p, n, n.left))
            stack.append((p, n, n.right))
        return ret
