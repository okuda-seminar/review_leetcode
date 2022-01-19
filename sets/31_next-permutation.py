#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
from typing import List


"""
time: O(len(nums))
space: O(1)
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            i -= 1
            if nums[i] < nums[i + 1]:
                idx = self.find_over_num(i + 1, nums[i], nums)
                nums[i], nums[idx] = nums[idx], nums[i]
                return self.slice_reverce(i + 1, nums)

        return self.slice_reverce(0, nums)

    def find_over_num(self, idx: int, num: int, nums: List[int]) -> int:
        for i in range(idx, len(nums)):
            if num >= nums[i]:
                return i - 1

        return len(nums) - 1

    def slice_reverce(self, num: int, nums: List[int]) -> List[int]:
        left = num
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
# @lc code=end
