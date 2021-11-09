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
from collections import deque


# use dfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

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


# use bfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        """compute the deepest leaves sum

        Args:
            root(Optional(TreeNode)): a binary tree

        Returns:
            int: deepeset leaves sum
        """
        queue = deque()
        queue.append(root)
        while queue:
            ans = 0
            for _ in range(len(queue)):
                cur = queue.popleft()
                ans += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return ans

# @lc code=end