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
            cur_root, depth = stack.pop()
            if not cur_root.right and not cur_root.left:
                min_depth = min(depth, min_depth)
                continue
            if cur_root.left:
                stack.append([cur_root.left, depth + 1])
            if cur_root.right:
                stack.append([cur_root.right, depth + 1])

        return min_depth
