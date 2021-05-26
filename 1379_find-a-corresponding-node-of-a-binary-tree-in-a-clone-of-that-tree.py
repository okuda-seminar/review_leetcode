# n = num of node of cloned
# time = O(n)
# space = O(n)
# done time = 10m


from collections import deque

class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not cloned:
            return cloned

        stack = deque([cloned])
        while stack:
            curr_node = stack.pop()
            if not curr_node:
                continue

            if curr_node.val == target.val:
                return curr_node

            stack.append(curr_node.left)
            stack.append(curr_node.right)
