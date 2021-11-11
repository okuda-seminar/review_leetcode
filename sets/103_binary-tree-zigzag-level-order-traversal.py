#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """return zigzag level order traversal of its nodes' values
        
        Args:
            root(TreeNode): a binary tree
        
        Returns:
            bool: zigzag level order traversal of its nodes' values
        """      
        if not root:
            return []

        ans = []
        level = 0
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

            if cur_ans and level % 2 == 0:
                ans.append(cur_ans)
            elif cur_ans and level % 2 == 1:
                ans.append(cur_ans[::-1])
            level += 1

        return ans
# @lc code=end

