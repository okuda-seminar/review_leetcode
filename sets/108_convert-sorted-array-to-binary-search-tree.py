#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
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
n = len(nums)
time: O(n)
space: O(n)
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Return the binary search tree
        Args:
            nums(List[int]): ascending order
        Returns:
            Optional[TreeNode]: binary search tree
        """
        if not nums:
            return None
        
        half = len(nums)//2
        node = TreeNode(nums[half])

        node.left = self.sortedArrayToBST(nums[:half])
        node.right = self.sortedArrayToBST(nums[half+1:])

        return node


"""
n = len(nums)
time: O(n)
space: O(n)
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """Return the binary search tree
        Args:
            nums(List[int]): ascending order
        Returns:
            Optional[TreeNode]: binary search tree
        """
        if not nums:
            return None
        
        half = len(nums)//2
        node = TreeNode(nums[half])
        queue = deque([(node, nums[:half], nums[half+1:])])

        while queue:
            cur, left, right = queue.popleft()
            if left:
                half = len(left)//2
                cur.left = TreeNode(left[half])
                queue.append([cur.left, left[:half], left[half+1:]])
            if right:
                half = len(right)//2
                cur.right = TreeNode(right[half])
                queue.append([cur.right, right[:half], right[half+1:]])
        return node
# @lc code=end
