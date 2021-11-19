#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
"""
n = len(grid)
m = len(grid[0])
time complexity : O(nm)
space complexity : O(1)
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """compute the islands

        Args:
            grid(List[List[str]]) : m * n 2D binary grid
        
        Returns:
            int: the number of islands
        """
        if len(grid) == 0:
            return None
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans += 1
                    self.dfs(i, j, grid)
        return ans
        
    def dfs(self, i, j, grid):
        """make the grid visited in the island

        Args:
            i(int): integer
            j(int): integer
            grid(List[List[str]]) : m * n 2D binary grid
        """
        if i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j:
            return

        if grid[i][j] == "1":
            grid[i][j] = "visited"
            self.dfs(i, j + 1, grid)
            self.dfs(i, j - 1, grid)
            self.dfs(i + 1, j, grid)
            self.dfs(i - 1, j, grid)
 # @lc code=end

