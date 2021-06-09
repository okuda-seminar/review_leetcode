#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
import collections


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        time: O(len(s))
        space: O(len(s))
        """
        s_counter = collections.Counter(s)
        palindrome_len = 0
        for num in s_counter.values():
            if num % 2 == 0:
                palindrome_len += num
            elif 1 < num and num % 2 != 0:
                palindrome_len += num - 1

        if palindrome_len != sum(s_counter.values()):
            palindrome_len += 1

        return palindrome_len
# @lc code=end
