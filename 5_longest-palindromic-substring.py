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
        """

        # use DP
        """
        time: O(n^2)   n : len(s)
        space: O(n^2)
        """
        if not s:
            return None

        check_palindromic_dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            check_palindromic_dp[i][i] = True

        max_len = 1
        palindromic_str = s[0]
        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s)):
                if s[start] == s[end] and (end - start == 1 or check_palindromic_dp[start + 1][end - 1]):
                    check_palindromic_dp[start][end] = True
                    if max_len < end - start + 1:
                        max_len = end - start + 1
                        palindromic_str = s[start: end + 1]
        return palindromic_str
# @lc code=end
