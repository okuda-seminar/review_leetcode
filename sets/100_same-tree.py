#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# use dfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """return true if the p and q are same trees

        Args:
            p(TreeNode): roots of binary trees
            q(TreeNode): roots of binary trees

        Returns:
            bool: return true if the p and q are same trees
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


# use bfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """return true if the p and q are same trees

        Args:
            p(TreeNode): roots of binary trees
            q(TreeNode): roots of binary trees

        Returns:
            bool: return true if the p and q are same trees
        """
        queue = deque()
        queue.append([p, q])

        while queue:
            cur_p, cur_q = queue.popleft()
            if not cur_p and not cur_q:
                continue

            if cur_p and cur_q:
                if cur_p.val != cur_q.val:
                    return False
                queue.append([cur_p.left, cur_q.left])
                queue.append([cur_p.right, cur_q.right])

            else:
                return False
        
        return True
# @lc code=end
