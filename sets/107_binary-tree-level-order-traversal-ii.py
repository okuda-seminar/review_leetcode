#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


# use bfs
"""
V = node nums
E = edge nums
time complexity : O(V + E)
space complexity : O(V)
"""

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """return level order traversal of its nodes' values
        
        Args:
            root(TreeNode): a binary tree
        
        Returns:
            bool: level order traversal of its nodes' values
        """
        queue = deque([root])
        ans = deque()
        while queue:
            cur_ans = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    queue.append(cur.left)
                    queue.append(cur.right)
                    cur_ans.append(cur.val)
            if cur_ans:
                ans.appendleft(cur_ans)

        return list(ans)
# @lc code=end
