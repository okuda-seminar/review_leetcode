#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        time: O(logn)
        space: O(1)
        """
        num_of_1_bit = 0
        for num in bin(n):
            if num == "1":
                num_of_1_bit += 1
        return num_of_1_bit
# @lc code=end

