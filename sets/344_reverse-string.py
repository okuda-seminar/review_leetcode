Q[344]. Reverse String

time : O(n)
space : O(1)

class Solution:
    def reverseString(self, s: List[str]) -> None:
        '''reverse characters
        Args:
            s(List[str]): string consist of lowercase
        Returns:
            None: reverse characters
        '''
        '''
        Do not return anything, modify s in-place instead.
        '''
        if not s:
            return ''

        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

