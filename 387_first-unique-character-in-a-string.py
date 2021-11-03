#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
from collections import Counter


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        time: O(n)
        space: O(n)
        n : len(s)
        """
        s_counter = Counter(s)
        for i in range(len(s)):
            if s_counter[s[i]] == 1:
                return i

        return -1
# @lc code=end
