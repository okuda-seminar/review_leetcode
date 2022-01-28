#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """Funtction to find the lowest common ancestor
        Args:
            root(TreeNode): a binary search tree
            p(TreeNode): a binary search tree
            q(TreeNode): a binary search tree
        Returns:
            TreeNode: the lowest common ancestor
        """
        p_num = p.val
        q_num = q.val
        cur = root
        while cur:
            if p_num < cur.val and q_num < cur.val:
                cur = cur.left
            
            elif cur.val < p_num and cur.val < q_num:
                cur = cur.right
            
            else:
                return cur
# @lc code=end

