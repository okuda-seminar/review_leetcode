#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        time: O(len(pattern))
        space: O(len(pattern))
        """
        ref = {}
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False

        for alph, word in zip(pattern, s_list):
            if alph in ref:
                if word != ref[alph]:
                    return False

            elif word in ref.values():
                return False

            else:
                ref[alph] = word

        return True

# @lc code=end

