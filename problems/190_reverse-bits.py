#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        """
        time : O(1)
        space : O(1)
        """
        return int((bin(n).replace("0b", "0" * (34 - len(str(bin(n))))))[::-1], 2)
# @lc code=end

