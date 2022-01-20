'''
Q[1219]. Path with Maximum Gold
'''

# n = len(grid)
# time : O(n**2)
# space : O(1)


from typing import List


class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        '''Return the maximum sum of path
        Args:
            grid(List[List[int]]): grid of m*n (1 <= len(grid) <= 15)
        Returns:
            int: the maximum sum of path
        '''
        if not grid:
            raise ValueError('grid should not be empty')
        
        self.ROW_LENGTH = len(grid)
        self.COL_LENGTH = len(grid[0])
        self.grid = grid
        max_gold = 0
        
        for i in range(self.ROW_LENGTH):
            for j in range(self.COL_LENGTH):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, self.backtracking(i, j))
        
        return max_gold
        
    def backtracking(self, i: int, j: int) -> int:
        '''Backtrack
        Args:
            i(int): row index
            j(int): column index
        Returns:
            int: the maximum sum of path
        '''
        if i < 0 or i >= self.ROW_LENGTH or j < 0 or j >= self.COL_LENGTH or self.grid[i][j] <= 0:
            return 0
        
        self.grid[i][j] *= -1

        down = self.backtracking(i + 1, j)
        up = self.backtracking(i - 1, j)
        right = self.backtracking(i, j + 1)
        left = self.backtracking(i, j - 1)
        
        self.grid[i][j] *= -1
        return self.grid[i][j] + max(down, up, left, right)
