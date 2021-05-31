#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        time: O(len(s))
        space: O(1)
        """
        for i in range(len(s) // 2):
            s[i], s[- i - 1] = s[- i - 1], s[i]
        return s

# @lc code=end

