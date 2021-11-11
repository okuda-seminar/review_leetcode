'''
Q[108]. Convert Sorted Array to Binary Search Tree

n = len(nums)
time : O(n)
space : O(n)
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''convert to binary search tree
        Args:
            nums(List[int]): an array consist of integers (1 <= len(nums) <= 10**4)
        Returns:
            TreeNode: binary search tree
        '''
        if not nums:
            return None

        middle = len(nums) // 2
        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle + 1:])
        return root
