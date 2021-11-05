'''
Q[389]. Find the Difference
'''

# n = len(t)
# time : O(nlogn)
# space : O(n)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''find the difference between s and t
        Args:
            s(str): string consist of lower case (0 <= len(s) <= 1000)
            t(str): string consist of lower case (len(t) = len(s) + 1)
        Returns:
            str: the difference between s and t
        '''
        if len(s) < 0 or len(s) > 1000:
            raise ValueError('s length should be [0, 1000]')

        if len(t) != len(s) + 1:
            raise ValueError('t length should be s length + 1')

        s_list = list(s)
        t_list = list(t)
        s_list.sort()
        t_list.sort()
        if len(set(s_list)) != len(set(t_list)):
            return ''.join(set(t_list) - set(s_list))

        for i in range(len(s_list)):
            if s_list[i] != t_list[i]:
                return t_list[i]

        return t_list[-1]


# n = len(t)
# time : O(n)
# space : O(n)

from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_count = Counter(t) 
        for char in s:
            t_count[char] -= 1
        
        for key, val in t_count.items():
            if val == 1:
                return key

# n = len(t)
# time : O(n**2)
# space : O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if s.count(char) != t.count(char):
                return char
