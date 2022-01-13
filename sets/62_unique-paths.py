#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
import math


# @lc code=start
"""
time: O(m + n)
space: O(1)
"""
class Solution:
    def uniquePaths1(self, m: int, n: int) -> int:
        """
        Args:
            m(int): integer
            n(int): integer
        Returns:
            int: the number of possible unique paths
        """
        if m == 0 or n == 0:
            return 0

        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))


"""
time: O(m * n)
space: O(m * n)
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Args:
            m(int): integer
            n(int): integer
        Returns:
            int: the number of possible unique paths
        """
        if m == 0 or n == 0:
            return 0

        dp = [[1] * n for _ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        
        return dp[-1][-1]
# @lc code=end
