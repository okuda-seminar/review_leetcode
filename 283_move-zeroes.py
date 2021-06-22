#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        time: O(len(nums))
        space: O(1)
        """
        non_zero_idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_idx] = nums[non_zero_idx], nums[i]
                non_zero_idx += 1
        return nums
# @lc code=end
