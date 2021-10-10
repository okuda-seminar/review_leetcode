#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        time: O(1)
        space: O(len(l))  l : number of words
        """
        return len(s.split()[-1]) if s.split() else 0
# @lc code=end

