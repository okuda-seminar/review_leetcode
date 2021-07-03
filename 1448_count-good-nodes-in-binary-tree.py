# n = node num of root
# time = O(n)
# space = O(n)
# done time = 20m


from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        stack = deque([[root, root.val]])
        good_nodes_count = 0

        while stack:
            cur_node, max_val = stack.pop()
            if cur_node is None:
                continue
            if max_val <= cur_node.val:
                good_nodes_count += 1
                max_val = cur_node.val
            stack.append([cur_node.left, max_val])
            stack.append([cur_node.right, max_val])

        return good_nodes_count
