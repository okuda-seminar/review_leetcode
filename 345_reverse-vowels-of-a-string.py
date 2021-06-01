#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        time: O(len(s))
        space: O(len(s))
        """
        list_s = list(s)
        left = 0
        right = len(s) - 1
        vowels = "aiueoAIUEO"
        while left < right:
            if list_s[right] in vowels and list_s[left] in vowels:
                list_s[right], list_s[left] = list_s[left], list_s[right]
                left += 1
                right -= 1
            elif not list_s[left] in vowels:
                left += 1
            elif not list_s[right] in vowels:
                right -= 1
        return ''.join(list_s)
# @lc code=end
