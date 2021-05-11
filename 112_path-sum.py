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
            cur_root, targetSum_rest = stack.pop()
            if not cur_root.left and not cur_root.right:
                if targetSum_rest == 0:
                    return True

            if cur_root.left:
                stack.append([cur_root.left, targetSum_rest - cur_root.left.val])
            if cur_root.right:
                stack.append([cur_root.right, targetSum_rest - cur_root.right.val])

        return False
