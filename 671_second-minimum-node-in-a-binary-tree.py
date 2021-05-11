# n = node_vals.length
# time = O(nlogn)
# space = O(n)
# done time = 15m


from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        stack = deque([root])
        node_vals = set()
        while stack:
            node = stack.popleft()
            if node is None:
                continue
            node_vals.add(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return sorted(node_vals)[1] if 2 <= len(node_vals) else -1
