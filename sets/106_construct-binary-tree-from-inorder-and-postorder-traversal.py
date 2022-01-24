#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """Function to build tree
        Args:
            inorder(List[int]): inorder traversal of the tree
            postorder(List[int]): postorder traversal of the tree
        Returns:
            Optional[TreeNode]: TreeNode
        """
        if not inorder or not postorder:
            return None
        
        node = TreeNode(postorder.pop())
        idx = inorder.index(node.val)

        node.right = self.buildTree(inorder[idx + 1:], postorder)
        node.left = self.buildTree(inorder[: idx], postorder)

        return node
# @lc code=end
