from collections import List
"""
Q DP
m : the length of a row in an array called grid
n : the length of a col in an array called grid
time complexity = O(mn)
space complexity = O(1)
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """get the minimum of path sum
        Args:
            grid (List[List[int]]): m x n grid filled with non-negative numbers
        Returns:
            the number which minimizes the sum of all numbers along its path
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif i > 0:
                    grid[i][j] += grid[i-1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j-1]
        return grid[-1][-1]