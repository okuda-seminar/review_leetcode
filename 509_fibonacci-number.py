#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        """
        time: O(n)
        space: O(1)
        """
        if n < 2:
            return n

        pre_fib_nums = 0
        fib_num = 1
        for n in range(2, n + 1):
            pre_fib_nums, fib_num = fib_num, fib_num + pre_fib_nums
        return fib_num
# @lc code=end
