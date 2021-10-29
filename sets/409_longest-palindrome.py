'''
Q[409]. Longest Palindrome

n = len(s)
time : O(n)
space : O(n)
'''

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''compute the length of the longest palindrome
        Args:
            s(str): string consist of English letters (1 <= len(s) <= 2000)
        Returns:
            int: the length of the longest palindrome
        '''
        if not s:
            raise ValueError('s length should be [1, 2000]')

        s_count = Counter(s)
        longest_palindrome = 0
        for val in s_count.values():
            if val % 2 == 0:
                longest_palindrome += val
            else:
                longest_palindrome += val - 1

        if longest_palindrome == len(s):
            return longest_palindrome

        return longest_palindrome + 1
