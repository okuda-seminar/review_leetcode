"""
dfs(iterative)
n = number of root node
time = O(n)
space = O(n)
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        if not root:
            return ans
        
        stack = [root]
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        return ans

"""
dfs(recursive)
n = number of root node
time = O(n)
space = O(n)
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.output = []
        self.dfs(root)
        return self.output
        
    def dfs(self, root:'Node')-> None:
        if not root:
            return None
        
        self.output.append(root.val)
        for child in root.children:
            self.dfs(child)