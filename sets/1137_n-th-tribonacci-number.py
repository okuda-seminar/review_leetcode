'''
Question :

The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Answer :
'''
class Solution:

    ''' DP : O(n)
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n <= 2:
            return 1

        first_num = 0
        second_num = 1
        third_num = 1
        for n in range(3, n + 1):
            first_num, second_num, third_num = second_num, third_num,\
                first_num + second_num + third_num
        return third_num
    '''

    ''' DP : O(n)
    def tribonacci(self, n: int) -> int:
        tri_arr = [0, 1, 1]
        for i in range(3, n + 1):
            tri_arr[i % 3] = sum(tri_arr)
        return tri_arr[n % 3]
    '''

    ''' memorization using lru_cache : O(n)

    from functools import lru_cache

    @lru_cache
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n <= 2:
            return 1

        return self.tribonacci(n - 1) + self.tribonacci(n - 2)\
               + self.tribonacci(n - 3)
    '''

    ''' memorization : O(n)

    def __init__(self):
        self.memo = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n <= 2:
            return 1

        if n in self.memo:
            return self.memo[n]

        res = self.tribonacci(n - 1) + self.tribonacci(n - 2)\
              + self.tribonacci(n - 3)
        self.memo[n] = res
        return res
    '''
