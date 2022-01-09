#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#

# @lc code=start
"""
time: O(n)
space: O(n)
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """Function to return possible sum
        Args:
            nums(List[int]): circular integer array 
        Returns:
            int: the maximum possible sum
        """
        if not nums:
            return

        if len(nums) == 1:
            return nums[0]

        max_sum_to_end = -float("inf")
        min_sum_to_end = float("inf")
        max_dp = [None] * len(nums)
        min_dp = [None] * (len(nums) - 1)
        for end in range(len(nums)):
            max_sum_to_end = max(nums[end], nums[end] + max_sum_to_end)
            min_sum_to_end = min(nums[end], nums[end] + min_sum_to_end)
            max_dp[end] = max_sum_to_end
            if end < len(nums) - 1:
                min_dp[end] = min_sum_to_end

        return max(max(max_dp), sum(nums) - min(min_dp))
# @lc code=end
