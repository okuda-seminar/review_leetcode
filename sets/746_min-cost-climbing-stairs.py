'''
Question:
You are given an integer array cost where cost[i] is 
the cost of ith step on a staircase. Once you pay the cost,
you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Answer:
'''
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''Compute the minimum total cost

        Args:
            cost(List[int]) : cost of steps (2 <= len(cost) <= 1000)
            
        Returns:
            int : minimum total cost
        
        '''
        if len(cost) <= 1:
            raise ValueError('len(cost) should be [2, 1000]')
            
        cost_size = len(cost)
        dp = [0] * size
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, cost_size):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        
        return min(dp[cost_size-2], dp[cost_size-1])
