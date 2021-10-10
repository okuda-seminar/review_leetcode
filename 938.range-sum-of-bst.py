#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
V = node nums
time complexity : O(V)
space complexity : O(1)
"""


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """compute sum of the all nodes with a value in the range [low, high]

        Args:
            root(Optional(TreeNode)): a binary tree
            low(int): integer
            high(int): integer

        Returns:
            int: sum of the all nodes with a value in the range [low, high]
        """
        self.low = low
        self.high = high
        self.range_sum = 0
        self.dfs(root)
        return self.range_sum

    def dfs(self, root: Optional[TreeNode]):
        """compute the sum

        Args:
            root(Optional(TreeNode)): a binary tree
        """
        if not root:
            return None

        if self.low <= root.val <= self.high:
            self.range_sum += root.val

        self.dfs(root.left)
        self.dfs(root.right)
# @lc code=end
