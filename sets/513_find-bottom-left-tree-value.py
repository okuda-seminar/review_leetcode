#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
from collections import deque


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# use bfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""
class Solution:
    def findBottomLeftValue1(self, root: Optional[TreeNode]) -> int:
        """Find bottom left tree value
        
        Args:
            root(Optional[TreeNode]): the root of a binary tree
        
        Returns:
            int: the leftmost value in the last row of the tree
        """
        if not root:
            return None

        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                cur = queue.popleft()
                if i == 0:
                    ans = cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans


# use dfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        """Find bottom left tree value
        
        Args:
            root(Optional[TreeNode]): the root of a binary tree
        
        Returns:
            int: the leftmost value in the last row of the tree
        """
        if not root:
            return None
        
        level = 1
        ans_level = 0
        stack = deque([(level, root)])
        while stack:
            level, cur = stack.pop()
            if cur:
                if ans_level < level:
                    ans = cur.val
                    ans_level = level
                stack.append([level + 1, cur.right])
                stack.append([level + 1, cur.left])
        return ans
# @lc code=end
