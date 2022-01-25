#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


"""
time: O(V)
space: O(V)
"""
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """Function to flatten tree
        Args:
            root(Optional[TreeNode]): a binary tree
        Returns:
            root(Optional[TreeNode]): flatten the tree
        """
        if not root:
            return None
        
        node = root
        stack = deque()

        while node or stack:
            if node.left:
                if node.right:
                    stack.append(node.right)
                node.right = node.left
                node.left = None
                node = node.right
            
            elif node.right:
                node = node.right
            
            else: 
                if stack:
                    node.right = stack.pop()
                    node = node.right
                else:
                    break
        
        return root
# @lc code=end
