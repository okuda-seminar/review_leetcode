"""
A1 DFS
n = number of root.val
time = O(n)
space = O(1)
"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """search minimum depth
        Args:
            root (TreeNode): binary tree
        Returns:
            ing: minimum depth
        Examples:
            minDepth([3,8,15,null,null,6,4]) <- 2
        """
        if not root:
            return 0
        if not root.right and not root.left:
            return 1
        elif not root.left:
            return self.minDepth(root.right) + 1
        elif not root.right:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
"""
A2 bfs
n = number of node
time = O(n)
space = O(1)
"""
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """search minimum depth
        Args:
            root (TreeNode): binary tree
        Returns:
            ing: minimum depth
        Examples:
            minDepth([3,8,15,null,null,6,4]) <- 2
        """
        if not root:
            return 0
        visited_queue = deque([(root,1)])
        while len(visited_queue) != 0:
            next_visit, cur_depth = visited_queue.popleft()
            if not next_visit.left and not next_visit.right:
                return cur_depth
            if next_visit.left:
                visited_queue.append((next_visit.left, cur_depth + 1))
            if next_visit.right:
                visited_queue.append((next_visit.right, cur_depth + 1))