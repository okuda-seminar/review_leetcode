# V = node num
# time: O(V)
# space: O(V)

from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ret = []
        stack = deque([(root, 1)])
        while stack:
            node, depth = stack.popleft()
            if node is None:
                continue
            if len(ret) < depth:
                ret.append([node.val])
            else:
                ret[-1].append(node.val)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
            
        return ret[::-1]
