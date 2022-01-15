#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
"""
n: len(prices)
time: O(n)
space: O(n)
"""
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Fuction to calculate the maximum profit
        Args:
            prices(List[int]): prices[i] is the price of a given stock on the ith day
        Returns:
            int: the maximum profit you can achieve
        """
        if not prices:
            return 0
        
        dp = [0] * (len(prices) + 1)
        min_price = prices[0]
        for i in range(1, len(prices) + 1):
            min_price = min(min_price, prices[i - 1] - dp[i - 2])
            dp[i] = max(dp[i - 1], prices[i - 1] - min_price)
        
        return dp[-1]
# @lc code=end
