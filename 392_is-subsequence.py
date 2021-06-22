#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        time: O(len(t))
        space: O(1)
        """
        if not len(s):
            return True

        elif not len(t):
            return False

        s_index, t_index = 0, 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
            t_index += 1
        return s_index == len(s)
# @lc code=end
