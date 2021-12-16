'''
Q[1638]. Count Substrings That Differ by One Character
'''

# n = len(s)
# m = len(t)
# time : O(n * m)
# space = O(1)


class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        '''Return the number of substrings
        Args:
            s(str): string (1 <= len(s) <= 100)
            t(str): string (1 <= len(t) <= 100)
        Returns:
            str: the number of substrings
        '''
        self.s = s
        self.t = t
        return sum(self.count(i, 0) for i in range(len(self.s))) + sum(self.count(0, j) for j in range(1, len(self.t)))

    def count(self, i: int, j: int) -> int:
        '''Count substrings
        Args:
            i(int): index
            j(int): index
        Returns:
            int: the number of substrings
        '''
        sub_count = pre_count = cur_count = 0
        for k in range(min(len(self.s) - i, len(self.t) - j)):
            cur_count += 1
            if self.s[i + k] != self.t[j + k]:
                pre_count, cur_count = cur_count, 0
            sub_count += pre_count
        return sub_count
