#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        time: O(len(nums))
        space: O(len(nums))
        """
        if not nums:
            return None

        ref = {}
        for num in nums:
            if num in ref:
                ref[num] += 1
            else:
                ref[num] = 1
            if (len(nums) / 2) <= ref[num]:
                return num

        return None

# @lc code=end

