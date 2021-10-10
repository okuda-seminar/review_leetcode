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
            cur_node = stack.popleft()
            if cur_node is None:
                continue
            node_vals.add(cur_node.val)
            stack.append(cur_node.left)
            stack.append(cur_node.right)
        return sorted(node_vals)[1] if 2 <= len(node_vals) else -1
