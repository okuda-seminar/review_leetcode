#
# @lc app=leetcode id=292 lang=python3
#
# [292] Nim Game
#

# @lc code=start
class Solution:
    def canWinNim(self, n: int) -> bool:
        """
        time: O(1)
        space: O(1)
        """
        return n % 4 != 0
# @lc code=end

