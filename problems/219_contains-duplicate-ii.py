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

        num_position = {}
        for i in range(len(nums)):
            if nums[i] in num_position and abs(i - num_position[nums[i]]) <= k:
                return True

            num_position[nums[i]] = i
        return False
# @lc code=end

