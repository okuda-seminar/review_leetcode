#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
from collections import Counter


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use sorting
        """
        time: O(nlogn)   n : len(max(s, t))
        space: O(len(n))
        sorted_s = ','.join(sorted(s))
        sorted_t = ','.join(sorted(t))
        return sorted_s == sorted_t
        """

        # use collections.Counter
        """
        time: O(n)   n : len(max(s, t))
        space: O(n)
        """
        return Counter(s) == Counter(t)
# @lc code=end

