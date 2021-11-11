#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """return level order traversal of its nodes' values
        
        Args:
            root(TreeNode): a binary tree
        
        Returns:
            bool: level order traversal of its nodes' values
        """
        if not root:
            return []
        
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            cur_ans = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    cur_ans.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
            if cur_ans:
                ans.append(cur_ans)

        return ans
# @lc code=end

