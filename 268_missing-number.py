#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
import collections

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use sorting
        """
        time: O(nlogn) n : len(nums)
        space: O(1)
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
        """

        """
        time: O(n) n : len(nums)
        space: O(n)
        """
        set_nums = set(nums)
        for i in range(len(nums) + 1):
            if i in set_nums:
                continue
            return i
# @lc code=end

