#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
V: number of node
time: O(VlogV)
space: O(V)
"""
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Function to recover Tree
        Args:
            root(Optional[TreeNode]): Tree
        Returns:
            Optional[TreeNode]: BST
        """
        self.temp = []
        self.dfs(root)
        nums = sorted(node.val for node in self.temp)
        for i in range(len(nums)):
            self.temp[i].val = nums[i]
        return root
    
    def dfs(self, cur: Optional[TreeNode]) -> None:
        """Function to write inorder
        Args:
            root(Optional[TreeNode]): Tree
        Returns:
            None
        """
        if not cur:
            return
        
        self.dfs(cur.left)
        self.temp.append(cur)
        self.dfs(cur.right)       
# @lc code=end
