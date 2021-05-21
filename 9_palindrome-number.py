#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        time: O(len(x))
        space: O(len(x))
        """
        if 2 ** 31 < abs(x):
            return 0
        x = str(x)
        return x == x[:: -1]

# @lc code=end

