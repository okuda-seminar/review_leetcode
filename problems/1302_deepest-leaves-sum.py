# V = node nums
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
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        ret = 0
        depth = 1
        stack = deque([[1, root]])
        while stack:
            d, n = stack.popleft()
            if n is None:
                continue
            if d == depth:
                ret += n.val
            else:
                ret = n.val
                depth = d
            stack.append([d + 1, n.left])
            stack.append([d + 1, n.right])
        return ret
