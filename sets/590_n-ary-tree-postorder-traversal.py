#
# @lc app=leetcode id=590 lang=python3
#
# [590] N-ary Tree Postorder Traversal
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque


"""
time: O(V)
space: O(V)
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """Function to make postorder
        Args:
            root(Node): Node
        Returns:
            List[int]: postorder list
        """
        if not root:
            return None
        
        stack = deque([root])
        res = deque()
        while stack:
            cur = stack.pop()
            res.appendleft(cur.val)
            for child in cur.children:
                stack.append(child)
        
        return list(res)
# @lc code=end
