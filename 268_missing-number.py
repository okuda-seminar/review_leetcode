#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        time: O(nlogn) n : len(nums)
        space: O(1)
        """
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
# @lc code=end

