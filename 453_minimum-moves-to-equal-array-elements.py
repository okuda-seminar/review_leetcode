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
        space: O(1)
        """
        min_moves_num = 0
        min_num = min(nums)
        for num in nums:
            min_moves_num += num - min_num
        return min_moves_num
# @lc code=end
