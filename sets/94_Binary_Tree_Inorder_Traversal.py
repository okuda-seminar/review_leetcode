"""
recursion
n = length of tree node
time = O(n)
space = O(n)
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.traversal = []
        if not root:
            return self.traversal
        
        self.recursion(root)
        return self.traversal
    
    def recursion(self, root: TreeNode) -> None:
        if root.left:
            self.recursion(root.left)
        self.traversal.append(root.val)
        if root.right:
            self.recursion(root.right)

"""
dfs
n = length of tree node
time = O(n)
space = O(n)
"""
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        ans, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                ans.append(node.val)
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
        
        return ans