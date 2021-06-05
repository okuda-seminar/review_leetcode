#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
import collections


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        time: O(n)
        space: O(n)
        n : max(len(ransomNote), len(magazine))
        """
        ransomNote_dict = collections.Counter(ransomNote)
        magazine_dict = collections.Counter(magazine)

        for alph in ransomNote_dict:
            if magazine_dict[alph] < ransomNote_dict[alph]:
                return False

        return True
# @lc code=end
