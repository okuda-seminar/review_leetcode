# n = the number of nodes
# time = O(n)
# space = O(n)
# done time = 15m


from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depth = 1
        min_depth = float('inf')
        stack = deque([[root, depth]])

        while stack:
            cur_node, depth = stack.pop()
            if cur_node:
                if not cur_node.right and not cur_node.left:
                    min_depth = min(depth, min_depth)
                stack.append([cur_node.left, depth + 1])
                stack.append([cur_node.right, depth + 1])

        return min_depth
