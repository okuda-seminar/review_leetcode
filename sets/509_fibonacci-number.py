'''
Question :
The Fibonacci numbers, commonly denoted F(n) form a sequence, called
the Fibonacci sequence, such that each number is the sum of the two
preceding ones, starting from 0 and 1.

Answer :
'''
class Solution:
    DP : O(n)

    def fib(self, n: int) -> int:
        '''Compute nth fib number
        Args:
            n(int): numbers of fib
        Returns:
            int: nth fib number
        '''
        if n < 2:
            return n

        pre_fib_num = 0
        fib_num = 1
        for n in range(2, n + 1):
            pre_fib_num, fib_num = fib_num, fib_num + pre_fib_num
        return fib_num
    

    memorization using lru_cache : O(n)

    from functools import lru_cache

    @lru_cache()
    def fib(self, n: int) -> int:
        '''Compute nth fib number
        Args:
            n(int): numbers of fib
        Returns:
            int: nth fib number
        '''
        if n < 2:
            return n

        return self.fib(n - 1) + self.fib(n - 2)

    memorization : O(n)

    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        '''Compute nth fib number
        Args:
            n(int): numbers of fib
        Returns:
            int: nth fib number
        '''
        if n < 2:
            return n

        if n in self.memo:
            return self.memo[n]

        res = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = res
        return res
