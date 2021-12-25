# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
dfs
n = number of node
e = number of edge
time = O(n+e)
space = O(n)
"""
from typing import Optional, List
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res
    
    def dfs(self, root: Optional[TreeNode], target: int, sub: List[int], res: List[List[int]]) -> List[List[int]]:
        if root:
            if root.right is None and root.left is None and root.val == target:
                sub.append(root.val)
                res.append(sub)
                return res
    
            self.dfs(root.right, target - root.val, sub + [root.val], res)
            self.dfs(root.left, target - root.val, sub + [root.val], res)
        return []