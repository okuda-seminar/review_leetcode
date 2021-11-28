#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# bfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Search in a binary search tree
        Args:
            root(Optional[TreeNode]): a binary search tree
            val(int): integer
        Returns:
            the subtree rooted with val
        """
        queue = deque([(root)])
        while queue:
            cur = queue.popleft()
            if cur.val == val:
                return cur
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        
        return None


# dfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """Search in a binary search tree
        Args:
            root(Optional[TreeNode]): a binary search tree
            val(int): integer
        Returns:
            the subtree rooted with val
        """
        stack = deque([(root)])
        while stack:
            cur = stack.pop()
            if cur.val == val:
                return cur
            
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        
        return None
# @lc code=end
