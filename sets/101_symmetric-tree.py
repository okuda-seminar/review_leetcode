#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        """Check whether the left and right are mirrored or not
        
        Args:
            root(TreeNode): a binary tree
        
        Returns:
            bool: return true if left and right are mirror
        """
        if not root:
            return True
        return self.check_mirror(root.left, root.right)

    def check_mirror(self, left: TreeNode, right: TreeNode) -> bool:
        """Check whether the left and right are mirrored or not
        
        Args:
            left(TreeNode): a binary tree
            right(TreeNode): a binary tree
        
        Returns:
            bool: return true if left and right are mirror
        """
        if not left and not right:
            return True

        if not left or not right:
            return False

        if left.val == right.val:
            outtree = self.check_mirror(left.left, right.right)
            intree = self.check_mirror(left.right, right.left)
            return outtree and intree

        return False


# use dfs by queue
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

class Solution:
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        """Check whether the left and right are mirrored or not
        
        Args:
            root(TreeNode): a binary tree
        
        Returns:
            bool: return true if left and right are mirror
        """
        if not root:
            return True

        stack = deque()
        stack.append([root.left, root.right])
        while stack:
            cur_left, cur_right = stack.pop()
            if not cur_left and not cur_right:
                continue

            if not cur_left or not cur_right:
                return False

            if cur_left.val != cur_right.val:
                return False

            stack.append([cur_left.left, cur_right.right])
            stack.append([cur_left.right, cur_right.left])

        return True


# use bfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """Check whether the left and right are mirrored or not
        
        Args:
            root(TreeNode): a binary tree
        
        Returns:
            bool: return true if left and right are mirror
        """
        if not root:
            return True

        queue = deque()
        queue.append([root.left, root.right])
        while queue:
            cur_left, cur_right = queue.popleft()
            if not cur_left and not cur_right:
                continue

            if not cur_left or not cur_right:
                return False

            if cur_left.val != cur_right.val:
                return False

            queue.append([cur_left.left, cur_right.right])
            queue.append([cur_left.right, cur_right.left])

        return True
# @lc code=end

