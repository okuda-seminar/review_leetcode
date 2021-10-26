"""
A.1 sort
n = len(nums)
time = O(n logn)
space = O(n)
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Args:
            nums (List[int]): array of integers (2 <= nums.length <= 500, 1 <= nums[i] <= 10^3)
        Returns:
            int: maximum value of (nums[i]-1)*(nums[j]-1)
        """
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
"""
A.2 heap
n = len(nums)
time = O(n)
space = O(n)
"""
import heapq
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Args:
            nums (List[int]): array of integers (2 <= nums.length <= 500, 1 <= nums[i] <= 10^3)
        Returns:
            int: maximum value of (nums[i]-1)*(nums[j]-1)
        """
        m, prev = heapq.nlargest(2, nums)
        return (m - 1) * (prev - 1)