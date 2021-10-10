# v = node num
# time : O(v)
# space : O(v)
# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = deque([root])
        ret = []
        while stack:
            value = 0
            length = 0
            for i in range(len(stack)):
                root = stack.popleft()
                if root is None:
                    continue
                value += root.val
                length += 1
                stack.append(root.left)
                stack.append(root.right)
            if length == 0:
                continue
            ret.append(value/length)
        return ret
