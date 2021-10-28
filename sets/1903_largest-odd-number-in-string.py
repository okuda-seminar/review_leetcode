'''
Q[1903]. Largest Odd Number in String

n = len(num)
time : O(n)
space : O(1)
'''


class Solution:
    def largestOddNumber(self, num: str) -> str:
        '''compute substring that is largest odd integer
        Args:
            num(str): string consist of digits (1 <= len(num) <= 10^5)
        Returns:
            str: substring that is largest odd integer
        '''
        if not num:
            return ''

        for i in reversed(range(len(num))):
            if int(num[i]) % 2 == 1:
                return num[:i+1]

        return ''
