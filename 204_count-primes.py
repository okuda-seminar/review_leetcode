#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        """
        time: O(n ** (3/2))
        space: O(n)
        """
        judge_p = [1] * n
        judge_p[0:2] = [0, 0]
        for num in range(int(n ** 0.5) + 1):
            if judge_p[num] == 1:
                for multiple in range(num ** 2, n, num):
                    judge_p[multiple] = 0
        return sum(judge_p)
# @lc code=end

