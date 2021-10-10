#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        """
        time: O(N)  N : the total of all nodes
        space: O(N)
        """
        if not root:
            return True

        left_node_depth = self.depth(root.left)
        right_node_depth = self.depth(root.right)
        return (abs(left_node_depth - right_node_depth) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, node: TreeNode) -> int:
        """
        calculate the node depth
        """
        if not node:
            return 0

        return max(self.depth(node.left), self.depth(node.right)) + 1
# @lc code=end

