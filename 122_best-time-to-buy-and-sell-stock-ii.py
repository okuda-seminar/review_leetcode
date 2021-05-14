#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time: O(len(prices))
        space: O(1)
        """
        sum_profit_to_day = 0
        for day in range(1, len(prices)):
            cur_price = prices[day]
            pre_price = prices[day - 1]
            if pre_price <= cur_price:
                sum_profit_to_day += cur_price - pre_price
        return sum_profit_to_day

# @lc code=end

