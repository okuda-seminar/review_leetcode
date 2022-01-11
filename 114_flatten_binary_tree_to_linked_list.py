from collections import Optional
"""
Q. stack
n : the number of tree node
time complexity = O(n)
space complexity = O(n)
"""


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            stack = [root]
            while stack:
                node = stack.pop()
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                    node.right = node.left
                    node.left = None
                elif stack:
                    node.right = stack[-1]


"""
Q. recursion
n : the number of tree node
time complexity = O(n)
space complexity = O(n)
"""


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.curr = TreeNode(None)
        self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None
        self.curr.left = None
        self.curr.right = root
        self.curr = root
        l, r = root.left, root.right
        self.dfs(l)
        self.dfs(r)