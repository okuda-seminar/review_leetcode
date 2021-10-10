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
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        time: O(N)  N : the total of all nodes
        space: O(N)
        """
        if not nums:
            return None

        half = len(nums) // 2
        node = TreeNode(nums[half])
        node.left = self.sortedArrayToBST(nums[:half])
        node.right = self.sortedArrayToBST(nums[half+1:])
        return node

# @lc code=end

