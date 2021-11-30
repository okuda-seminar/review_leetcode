"""
dfs
n = number of node
time = O(n)
space = O(1)
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Invert Tree
        Args:
            root (TreeNode) : Binary Tree
        Returns:
            TreeNodee: inverse binary tree
        """
        if not root:
            return None
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

"""
stack
n = number of node
time = O(n)
space = O(1)
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Invert Tree
        Args:
            root (TreeNode) : Binary Tree
        Returns:
            TreeNodee: inverse binary tree
        """
        inverse = root
        stack = [inverse]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
