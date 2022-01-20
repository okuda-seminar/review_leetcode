'''
Question:
Given a string s and an integer k, reverse the first k characters for every 2k\
characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are\
less than 2k but greater than or equal to k characters, then reverse the first\
k characters and left the other as original.

Answer:
'''
# O(n)
# n = s.length
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        '''reverse characters every 2k
        Args:
            s(str): string consist of lowercase
            k(int): number of reverse characters
        Returns:
            str: reverse characters every 2k
        '''
        if not s or k == 0:
            return ''

        s_list = list(s)
        for i in range(0, len(s), 2 * k):
            left = i
            if i + k - 1 < len(s):
                right = i + k - 1
            else:
                right = len(s) - 1

            while left < right:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        s_join = ''.join(s_list)
        return s_join
