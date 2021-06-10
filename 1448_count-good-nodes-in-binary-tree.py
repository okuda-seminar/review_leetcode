# n = node num of root
# time = O(n)
# space = O(n)
# done time = 20m


from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        stack = collections.deque([[root, root.val]])
        good_nodes_count = 0

        while stack:
            cur_node, max_val = stack.pop()
            if cur_node.val == max_val:
                good_nodes_count += 1
            if cur_node.left:
                stack.append([cur_node.left, max(max_val, cur_node.left.val)])
            if cur_node.right:
                stack.append([cur_node.right, max(max_val, cur_node.right.val)])

        return good_nodes_count
