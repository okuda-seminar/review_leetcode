# done time = 15m


from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: TreeNode) -> int:
        # use queue
        '''
        n = the number of nodes
        time = O(n)
        space = O(n)

        if root is None:
            return 0

        depth = 1
        min_depth = float('inf')
        stack = deque([[root, depth]])

        while stack:
            cur_node, depth = stack.pop()
            if cur_node:
                if cur_node.right is None and cur_node.left is None:
                    min_depth = min(depth, min_depth)
                stack.append([cur_node.left, depth + 1])
                stack.append([cur_node.right, depth + 1])

        return min_depth
        '''

        # use recursive funvtion
        '''
        n = the number of nodes
        h = the depth of tree
        time = O(n)
        space = O(h)
        '''

        if root is None:
            return 0

        if root.left is None or root.right is None:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
