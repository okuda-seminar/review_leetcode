#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
import collections


# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        time: O(len(t))
        space: O(len(t))
        """
        s_counter = collections.Counter(s)
        t_counter = collections.Counter(t)
        for alph in t_counter:
            if s_counter[alph] != t_counter[alph]:
                return alph
# @lc code=end
