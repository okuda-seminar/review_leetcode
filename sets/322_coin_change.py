import sys
from collections import List
"""
n: amount
m: the length of coins
time complexity = O(mn)
space complexity = O(mn)
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """coin change
        Args:
            coins (List[int]): coins of different denominations
            amount (int): total amount of money
        Returns:
            int: the fewest number of coins
        Examples:
            coinChange([1, 3, 5], 11) -> 3
        """
        if amount == 0:
            return 0
        dp = [[2**64 for _ in range(amount + 1)]for _ in range(len(coins) + 1)]
        for i in range(len(coins)+1):
            dp[i][0] = 0
        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                if j < coins[i - 1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], 1 + dp[i][j - coins[i - 1]])
        if dp[-1][-1] == 2**64:
            return -1
        else:
            return dp[-1][-1]


"""
n: amount
m: the length of coins
time complexity = O(mn)
space complexity = O(n)
"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [2**64 for _ in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        if dp[-1] == 2**64:
            return -1
        else:
            return dp[-1]


"""
n: amount
m: the length of coins
time complexity = O(m)
space complexity = O(1)
"""


class Solution:
    def recur(self, coins, amount, lookup):
        if amount not in lookup:
            if amount == 0:
                return 0
            minCoins = sys.maxsize
            for coin in coins:
                if amount-coin >= 0:
                    minCoins = min(minCoins, 1 + self.recur(coins, amount-coin, lookup))
            lookup[amount] = minCoins
        return lookup[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        minCoins = self.recur(coins, amount, {})
        if minCoins == sys.maxsize:
            return -1
        return minCoins