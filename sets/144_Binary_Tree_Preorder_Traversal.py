"""
dfs
n = length of tree node
time = O(n)
space = O(n)
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
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
                if node.left:
                    stack.append((node.left, False))
                stack.append((node, True))
        return ans