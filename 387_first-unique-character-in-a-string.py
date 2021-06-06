#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
import collections


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        time: O(n)
        space: O(1)
        n : len(s)
        """
        s_dict = collections.Counter(s)
        for i in range(len(s)):
            if s_dict[s[i]] == 1:
                return i

        return -1
# @lc code=end
