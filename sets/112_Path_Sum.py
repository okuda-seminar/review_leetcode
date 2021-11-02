"""
A recusion
n = number of node
time = O(n)
space = O(1)
"""
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """compute path sum
        Args:
            root (TreeNode): binary tree (-1000 <= Node.val <= 1000, 0 <= number of nodes <= 5000)
            targetSum (int): integer (-1000 <= targetSum <= 1000)
        Returns:
            bool: whether tree's path sum equal targetSum or not
        Examples:
            hasPathSum([5,4,8,11,null,13,4,7,2,null,null,null,1]) <- true
        """
        if not root:
            return False
        
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        targetSum -= root.val
        return self.hasPathSum(root.right, targetSum) or self.hasPathSum(root.left, targetSum)