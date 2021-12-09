# n = len(coins)
# m = target
# time : O(n * m)
# space : O(n * m)


from typing import List


class Solution:

    def coin_dp(self, coins: List[int], target: int) -> List[int]:
        '''Returns the minimum number of coins
        Args:
            coins(List[int]): the array of intgers
            target(int): the target price
        Returns:
            List[int]: the minimum number of coins
        '''
        if not coins:
            raise ValueError('coins should not be empty')

        dp = [[0]*(target + 1) for _ in range(len(coins) + 1)]

        for i in range(target + 1):
            dp[0][i] = float('inf')
        
        coin_kinds = len(coins)
        for i in range(coin_kinds + 1):
            dp[i][0] = 0
        
        coins.insert(0, 0)
        for i in range(1, coin_kinds + 1):
            for j in range(1, target + 1):
                if j < coins[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - coins[i]] + 1)

        return dp[-1][-1]
