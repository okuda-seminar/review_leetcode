#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        """
        time: O(len(nums))
        space: O(len(nums))
        """
        min_num = min(nums)
        return sum([num - min_num for num in nums])
# @lc code=end
