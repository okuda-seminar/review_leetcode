"""
n = the number of node
e = the number of edge
time complexity = O(n+e)
space complexity = O(n)
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Args:
            root (TreeNode): binary search tree
            k (int): the number of what is the smallest number
        Returns:
            int: the k th smallest value of all the values of node in the tree
        """
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            
            root = root.right