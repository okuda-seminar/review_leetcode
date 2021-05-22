#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        time: O(nlogn)   n : len(s)
        space: O(len(n))
        """
        sorted_s = ','.join(sorted(s))
        sorted_t = ','.join(sorted(t))
        return sorted_s == sorted_t
# @lc code=end

