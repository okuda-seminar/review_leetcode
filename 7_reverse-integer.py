#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """
        time: O(len(x))
        space: O(len(x))
        """
        if 0 <= x:
            x = str(x)
            output = int(x[::-1])
        else:
            x = str(-x)
            x = int(x[::-1])
            output = -x
        if 2 ** 31 < abs(output):
            return 0
        return output
        
# @lc code=end