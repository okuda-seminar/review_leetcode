#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
from collections import deque


# use bfs
"""
time complexity : O(n ** (3/2))
space complexity : O(n)
"""

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        """Return least number of perfect square numbers that sum to n
        
        Args:
            n(int): integer
        
        Returns:
            int: the least number of perfect square numbers that sum to n
        """
        ans = 0
        queue = deque([(ans, n)])
        visited = {0}
        while queue:
            level, cur = queue.popleft()
            level += 1
            squeare_root = 1
            while squeare_root ** 2 <= cur:
                if squeare_root ** 2 == cur:
                    return level
                
                if cur - squeare_root ** 2 not in visited:
                    visited.add(cur - squeare_root ** 2)
                    queue.append([level, cur - squeare_root ** 2])

                squeare_root += 1


# use dp
"""
time complexity : O(n ** (3/2)), some examples are TLE
space complexity : O(n)
"""

class Solution(object):
    def numSquares1(self, n):
        """Return least number of perfect square numbers that sum to n
        
        Args:
            n(int): integer
        
        Returns:
            int: the least number of perfect square numbers that sum to n
        """
        dp = [float('inf')]*(n+1)
        dp[0]=0
        for i in range(1, len(dp)):
            j = 1
            while j ** 2 <= i:
                dp[i] = min(dp[i], dp[i - j ** 2] + 1)
                j += 1

        return dp[-1]
# @lc code=end
