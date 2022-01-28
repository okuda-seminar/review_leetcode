#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Function to convert BST to Tree
        Args:
            root(TreeNode): a Binary Search Tree
        Returns:
            TreeNode: Greater Tree
        """
        cur_sum = 0
        stack = deque()
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur_sum += cur.val
            cur.val = cur_sum
            cur = cur.left

        return root
# @lc code=end

