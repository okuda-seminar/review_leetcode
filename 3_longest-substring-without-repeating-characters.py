#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        time: O(len(s))
        space: O(len(s))
        """
        ref = {}
        cur_max_length = 0
        start = 0
        for idx, alph in enumerate(s):
            if alph in ref:
                next_repeating_char = ref[alph] + 1
                if next_repeating_char > start:
                    start = next_repeating_char
            cur_max_length = max(idx - start + 1, cur_max_length)
            ref[alph] = idx
        return cur_max_length
# @lc code=end

