'''
Question :

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Answer :
'''
class Solution:

    DP : O(n)

    from collections import deque


    def tribonacci(self, n: int) -> int:
        '''Compute nth tibonacci number
        Args:
            n(int): number of tibonacci
        Returns:
            int: nth tibonacci number
        '''
        TRY_NUM = 3
        tri_arr = deque([0, 1, 1])
        if n < TRY_NUM:
            return tri_arr[n - 1]

        sum_tri_arr = sum(tri_arr)
        
        for i in range(TRY_NUM, n + 1):
            tri_arr.append(sum_tri_arr)
            sum_tri_arr += sum_tri_arr - tri_arr[0]
            tri_arr.popleft()

        return tri_arr[-1]

    memorization using lru_cache : O(n)

    from functools import lru_cache

    @lru_cache
    def tribonacci(self, n: int) -> int:
        '''Compute nth tibonacci number
        Args:
            n(int): number of tibonacci
        Returns:
            int: nth tibonacci number
        '''
        if n == 0:
            return 0

        if n <= 2:
            return 1

        return self.tribonacci(n - 1) + self.tribonacci(n - 2)\
               + self.tribonacci(n - 3)

    memorization : O(n)

    def __init__(self):
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        '''Compute nth tibonacci number
        Args:
            n(int): number of tibonacci
        Returns:
            int: nth tibonacci number
        '''
        if n == 0:
            return 0

        if n <= 2:
            return 1

        if n in self.memo:
            return self.memo[n]

        tri_sum = self.tribonacci(n - 1) + self.tribonacci(n - 2)\
              + self.tribonacci(n - 3)
        self.memo[n] = tri_sum
        return tri_sum
