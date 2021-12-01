#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """Calcurate the minimum absolute difference
        Args:
            root(Optional[TreeNode]):binary search tree
        Returns:
            int: the minimum absolute difference
        """
        if not root:
            return 0

        ans = float('inf')
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            if cur.left:
                ans = min(ans, cur.val - cur.left.val)
                queue.append(root.left)
            if cur.right:
                ans = min(ans, cur.right.val - cur.val)
                queue.append(root.right)
        return ans
# @lc code=end
