"""
n : the length of the column of obstacleGrid
m : the length of the row of obstacleGrid
time = O(m * n)
space = O(m * n)
"""
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """calcurate the number of unique paths with obstacles
        Args:
            obstacleGrid (List[List[int]]): an array containing location information of obstacles
        Returns:
            int: the number of unique paths
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j == 0:
                        dp[i][j] = 1
                    elif i == 0:
                        dp[i][j] = dp[i][j-1]
                    elif j == 0:
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]