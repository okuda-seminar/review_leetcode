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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        ref = {}
        stack = deque([root])
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if k - node.val in ref:
                return True
            ref[node.val] = 1
            stack.append(node.left)
            stack.append(node.right)
        return False
