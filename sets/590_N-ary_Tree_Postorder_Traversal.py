"""
dfs(iteratively)
n = number of nodes
time = O(n)
space = O(n)
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        """postorder traversal
        Args:
            root (Node): n-ary tree
        
        Returns:
            List[int]: postorder traversal of its nodes' values
            
        Examples:
            postorder([1,null,3,2,4,null,5,6]) -> [5,6,3,2,4,1]
        """
        if not root:
            return []

        stack = [(root)]
        output = []
        while stack:
            node = stack.pop()
            stack.extend(node.children)
            output.append(node.val)
        
        return output[::-1]