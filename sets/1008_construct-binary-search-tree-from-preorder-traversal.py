#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
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
time: O(len(preorder))
space: O(1)
"""
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        """Function to convert list to BST
        Args:
            preorder(List[int]): preorder traversal of a BST
        Returns:
            TreeNode: BST
        """
        if not preorder:
            return

        root = TreeNode(preorder[0])
        stack = deque([root])
        for num in preorder[1:]:
            if num < stack[-1].val:
                stack[-1].left = TreeNode(num)
                stack.append(stack[-1].left)
            else:
                while stack and stack[-1].val < num:
                    last = stack.pop()
                last.right = TreeNode(num)
                stack.append(last.right)
        return root
# @lc code=end
