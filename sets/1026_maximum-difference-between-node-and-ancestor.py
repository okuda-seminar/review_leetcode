#
# @lc app=leetcode id=1026 lang=python3
#
# [1026] Maximum Difference Between Node and Ancestor
#
from collections import deque


# use dfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """compute max difference

        Args:
            root(Optional(TreeNode)): treenode
        
        Returns:
            int: max ancestor difference 
        """
        self.ans = 0
        self.dfs(root, root.val, root.val)
        return self.ans

    def dfs(self, root: Optional[TreeNode], max_num, min_num):
        """compute max difference

        Args:
            root(Optional(TreeNode)): treenode
            max_num(int): the max number
            min_num(int): the minimum number
        """
        if not root:
            return None
        
        self.ans = max(self.ans, abs(root.val - max_num), abs(root.val - min_num))
        max_num = max(max_num, root.val)
        min_num = min(min_num, root.val)
        self.dfs(root.left, max_num, min_num)
        self.dfs(root.right, max_num, min_num)



# use dfs by queue
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """compute max difference

        Args:
            root(Optional(TreeNode)): treenode
        
        Returns:
            int: max ancestor difference 
        """
        stack = deque()
        print()
        stack.append([root, float("inf"), float("-inf")])
        ans = 0
        while stack:
            cur, min_num, max_num = stack.pop()
            if cur:
                min_num = min(min_num, cur.val)
                max_num = max(max_num, cur.val)
                ans = max(ans, max_num - min_num)
                stack.append([cur.left, min_num, max_num])
                stack.append([cur.right, min_num, max_num])

        return ans



# use bfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        """compute max difference

        Args:
            root(Optional(TreeNode)): treenode
        
        Returns:
            int: max ancestor difference 
        """
        queue = deque()
        queue.append([root, float("inf"), float("-inf")])
        ans = 0
        while queue:
            cur, min_num, max_num = queue.popleft()
            if cur:
                min_num = min(min_num, cur.val)
                max_num = max(max_num, cur.val)
                ans = max(ans, max_num - min_num)
                queue.append([cur.left, min_num, max_num])
                queue.append([cur.right, min_num, max_num])

        return ans
# @lc code=end
