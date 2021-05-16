# n = nodes num
# time = O(n)
# space = O(n)
# done time = 40m


from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        stack = deque([[root, targetSum - root.val]])
        while stack:
            cur_node, targetSum_rest = stack.pop()
            if not cur_node.left and not cur_node.right:
                if targetSum_rest == 0:
                    return True

            if cur_node.left:
                stack.append([cur_node.left, targetSum_rest - cur_node.left.val])
            if cur_node.right:
                stack.append([cur_node.right, targetSum_rest - cur_node.right.val])

        return False
