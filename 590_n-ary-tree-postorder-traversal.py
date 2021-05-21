# V = node num
# rimw: O(V)
# space: O(V)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def traverse(root):
            if root is None:
                return
            for c in root.children:
                traverse(c)
            ret.append(root.val)
            
        ret = []
        traverse(root)
        return ret
