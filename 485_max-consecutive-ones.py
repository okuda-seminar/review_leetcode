#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        time: O(len(nums))
        space: O(1)
        """
        cur_consecutive = 0
        max_consecutive = 0
        for num in nums:
            if num == 1:
                cur_consecutive += 1
            else:
                max_consecutive = max(max_consecutive, cur_consecutive)
                cur_consecutive = 0

        max_consecutive = max(max_consecutive, cur_consecutive)
        return max_consecutive
# @lc code=end
