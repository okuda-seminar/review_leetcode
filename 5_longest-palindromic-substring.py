#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        time: O(n^2)   n : len(s)
        space: O(1)
        """
        if len(s) == 1:
            return s

        max = s[0]
        for i in range(1, len(s)):
            left = right = i
            while 1 <= left and right <= (len(s) - 2):
                if s[left - 1] == s[right + 1]:
                    left -= 1
                    right += 1
                else:
                    break
            if len(max) < len(s[left:right + 1]):
                max = s[left:right + 1]

            if s[i] == s[i - 1]:
                left = i - 1
                right = i
                while 1 <= left and right <= (len(s) - 2):
                    if s[left - 1] == s[right + 1]:
                        left -= 1
                        right += 1
                    else:
                        break
                if len(max) < len(s[left:right + 1]):
                    max = s[left:right + 1]

        return max
# @lc code=end

