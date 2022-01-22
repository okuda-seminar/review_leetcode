#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
"""
n = len(nums)
time: O(n)
space: O(1)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        ans = 0
        max_step = 0
        cur_step = 0
        for idx, num in enumerate(nums):
            max_step = max(max_step, idx + num)
            if max_step >= len(nums) - 1:
                return ans + 1
            if idx == cur_step:
                cur_step = max_step
                ans += 1
# @lc code=end
