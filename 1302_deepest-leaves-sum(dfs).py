#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
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
space complexity : O(V)
"""


# use dfs
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """compute the deepest leaves sum

        Args:
            root(Optional(TreeNode)): a binary tree

        Returns:
            int: deepeset leaves sum
        """
        self.deepest_level = -1
        self.deepest_sum = 0
        self.dfs(root, 0)
        return self.deepest_sum

    def dfs(self, root: Optional[TreeNode], level: int):
        """compute the deepest leaves sum

        Args:
            root(Optional(TreeNode)): a binary tree
            level: depth of root.val
        """
        if not root:
            return None

        if self.deepest_level < level:
            self.deepest_level = level
            self.deepest_sum = root.val

        elif self.deepest_level == level:
            self.deepest_sum += root.val

        self.dfs(root.left, level + 1)
        self.dfs(root.right, level + 1)

# Examples: deepesetLeavesSum([1, 2, 3, null, 4, 5, null]) -> 9

# @lc code=end