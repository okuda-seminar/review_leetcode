"""
A bfs
n = number of root.node
time = O(n)
space = O(n)
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """return level order
        
        Args:
            root (optional[TreeNode]): binary tree
            
        Returns:
            List[List[int]]: the level order trabersal of its nodes' values
            
        Examples:
            levelOrder([3,9,20,null,null,15,7]) <- [[3], [9, 20], [15, 7]]
        """
        if not root:
            return root
        
        queue = [root]
        ans = []
        while queue:
            l = len(queue)
            level = []
            for i in range(l):
                curr_node = queue.pop(0)
                level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)
            ans.append(level)
        return ans