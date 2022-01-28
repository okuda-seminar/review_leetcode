#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Return the kth smallest value
        Args:
            root(TreeNode): the root of a binary search tree
            k(int): integer
        Returns:
            int: the kth smallest value
        """
        if not root:
            return None

        n = 0
        stack = deque()
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if stack:
                node = stack.pop()
                n += 1

            if n == k:
                return node.val
            
            root = node.right
# @lc code=end
