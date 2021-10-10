# v = node num
# time : O(v)
# space : O(v)

from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return None
        stack = deque([root])
        ret = []
        while stack:
            root = stack.pop()
            if root.children is None:
                continue
            for child in reversed(root.children):
                stack.append(child)
            ret.append(root.val)
        return ret
