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
        ref_char = {}
        ref_word = {}
        s_list = s.split()
        if len(pattern) != len(s_list):
            return False

        for alph, word in zip(pattern, s_list):
            if alph in ref_char:
                if word != ref_char[alph]:
                    return False

            else:
                ref_char[alph] = word

            if word in ref_word:
                if alph != ref_word[word]:
                    return False

            else:
                ref_word[word] = alph

        return True

# @lc code=end

