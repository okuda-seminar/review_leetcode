#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
from collections import Counter


# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        time: O(n)
        space: O(n)
        n : max(len(ransomNote), len(magazine))
        """
        ransomNote_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)

        for alph in ransomNote_counter:
            if magazine_counter[alph] < ransomNote_counter[alph]:
                return False

        return True
# @lc code=end
