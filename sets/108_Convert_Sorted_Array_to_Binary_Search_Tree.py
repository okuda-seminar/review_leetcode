"""
A
n = len(nums)
time = O(n logn)
space = O(n)
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """sorted BST
        Args:
            nums (List[int]): integer array (1 <= len(nums) <= 10^4, -10^4 <= nums[i] <= 10^4)
        Returns:
            TreeNode: sorted in ascending order
        Examples:
            sortedArrayToBST([-10, -3, 0, 3, 10]) <- [0, -3, 3, -10, null, null, 10]
        """
        if not nums:
            return None
        
        mean = len(nums) // 2
        tree = TreeNode(nums[mean])
        tree.right = self.sortedArrayToBST(nums[mean+1:])
        tree.left = self.sortedArrayToBST(nums[:mean])
        return tree