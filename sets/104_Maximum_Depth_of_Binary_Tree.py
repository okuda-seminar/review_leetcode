"""
A1 recursive
n = number of root.val
time = O(n)
space = O(1)
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """search maximum depth
        Args:
            root (TreeNode): treenode
        Returns:
            int: number of maximum depth
        Examples:
            maxDepth([3,9,20,null,null,15,7]) <- 3
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
"""
A2 bfs
n = number of node
time = O(n)
space = O(1)
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """search maximum depth
        Args:
            root (TreeNode): treenode
        Returns:
            int: number of maximum depth
        Examples:
            maxDepth([3,9,20,null,null,15,7]) <- 3
        """
        if not root:
            return 0
        depth = 0
        queue = [root]
        while queue:
            depth += 1
            for i in range(len(queue)):
                cur_queue = queue.pop(0)
                if cur_queue.left:
                    queue.append(cur_queue.left)
                if cur_queue.right:
                    queue.append(cur_queue.right)
        return depth