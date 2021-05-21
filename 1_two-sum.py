#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        time: O(n**2)
        space: O(1)
        
        n = len(nums)
        for i in range(n):
            ans = target - nums[i]
            for j in range(i+1, n):
                if ans == nums[j]:
                    return [i,j]
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        time: O(n)
        space: O(n)
        """
        if nums is None or target is None:
            return None
        ref = {}
        for idx, num in enumerate(nums):
            if target - num in ref:
                return [ref[target - num], idx]
            ref[num] = idx
# @lc code=end
