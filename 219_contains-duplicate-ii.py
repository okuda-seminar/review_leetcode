#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#

# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        time: O(len(nums))
        space: O(len(nums))
        """
        if not nums:
            return False

        ref = {}
        for i in range(len(nums)):
            if nums[i] in ref and abs(i - ref[nums[i]]) <= k:
                return True

            ref[nums[i]] = i
        return False
# @lc code=end

