"""
n = number of node in root
time = O(n)
space = O(1)
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """search a valid binary tree
        Args:
            root (TreeNode): binary tree
        
        Returns:
            bool: whether root is a valid binary tree
        
        Examples:
            isValidBST([2, 1, 3]) <- true
            isValidBST([4, 1, 3]) <- false
        """
        upper = float('inf')
        lower = float('-inf')
        return self.rangeBST(root, lower, upper)
        
    def rangeBST(self, root: Optional[TreeNode], lower: int, upper: int) -> bool:
        if not root:
            return True
        
        if lower < root.val < upper:
            return self.rangeBST(root.left, lower, root.val) \
                    and self.rangeBST(root.right, root.val, upper)

        else:
            return False
        