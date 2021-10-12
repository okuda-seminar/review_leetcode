'''
Question :
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct
ways can you climb to the top?

Answer :

Almost the same answer as 509
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        # DP : O(n)
        if n <= 1:
            return n

        pre_ways = 1
        cur_ways = 2
        for i in range(n - 2):
            pre_ways, cur_ways = cur_ways, pre_ways + cur_ways

        return cur_ways
