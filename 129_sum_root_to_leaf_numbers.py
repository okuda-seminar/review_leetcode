from typing import Optional
"""
dfs + recursion
n: number of node
e: number of edge
time complexity: O(n+e)
space complexity: O(n)
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Args:
            root (Optional[TreeNode]): binary tree containing digits from 0 to 9
        Returns:
            int: sum root to leaf numbers
        """
        self.sum = 0
        self.dfs(root, 0)
        return self.sum
        
    def dfs(self, node: Optional[TreeNode], num: int) -> None:
        if node is None:
            return None
        
        if node.right is None and node.left is None:
            self.sum += num * 10 + node.val
            return None
        
        self.dfs(node.right, num * 10 + node.val)
        self.dfs(node.left, num * 10 + node.val)
"""
dfs + stack
n: number of node
e: number of edge
time complexity: O(n+e)
space complexity: O(n)
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Args:
            root (Optional[TreeNode]): binary tree containing digits from 0 to 9
        Returns:
            int: sum root to leaf numbers
        """
        if root is None:
            return 0
        
        node_sum = 0
        res = 0
        stack = [(root, res)]
        while stack:
            node, res = stack.pop()
            res = res * 10 + node.val
            if node.right is None and node.left is None:
                node_sum += res
            if node.right:
                stack.append((node.right, res))
            if node.left:
                stack.append((node.left, res))
        return node_sum
    