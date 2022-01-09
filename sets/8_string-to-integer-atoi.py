#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
from re import match

"""
time: O(n)
space: O(1)
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        """Function to convert str to int
        Args:
            s(str): string
        Returns:
            int: integer
        """
        if not s:
            return

        ans = match(r'\s*([+-]?\d+)', s)
        if ans:
            if int(ans.group(1)) <= - 2 ** 31:
                return - 2 ** 31

            elif 2 ** 31 <= int(ans.group(1)):
                return 2 ** 31 - 1

            else:
                return int(ans.group(1))

        return 0
# @lc code=end
