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
    def isUnivalTree(self, root: TreeNode) -> bool:
        stack = deque([root])
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if node.val != root.val:
                return False
            stack.append(node.left)
            stack.append(node.right)
        return True
