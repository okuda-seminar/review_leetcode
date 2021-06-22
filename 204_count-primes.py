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
        judge_prime_num = [1] * n
        judge_prime_num[0:2] = [0, 0]
        for num in range(int(n ** 0.5) + 1):
            if judge_prime_num[num] == 0:
                continue
            for multiple_of_num in range(num ** 2, n, num):
                judge_prime_num[multiple_of_num] = 0
        return sum(judge_prime_num)
# @lc code=end

