#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
"""
time: n^2
space: n
"""
class Solution:
    def numTrees(self, n: int) -> int:
        """Return the number of structurally unique BST's
        Args:
            n: integer
        Returns:
            int: the number of structurally unique BST's
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[-1]
# @lc code=end

