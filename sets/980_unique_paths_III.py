"""
m : length of the row of grid
n : length of the column of grid
count : the number of 0 in grid
time complexity = O(max(m*n, 4^count))
space complexity = O(4^count)
"""
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """calcurate unique path
        Args:
            grid (List[List[int]]): an integer array
        Returns:
            int: the number of 4-directional walks
        """
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.result = 0
        start = None
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    start = (i, j, count)
        self.backtrack(start[0], start[1], count)
        return self.result
    
    def backtrack(self, row: int, col: int, count: int) -> None:
        for x, y in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
            if 0 <= x < self.m and 0 <= y < self.n:
                if self.grid[x][y] == 0:
                    self.grid[x][y] = -1
                    self.backtrack(x, y, count - 1)
                    self.grid[x][y] = 0
                elif self.grid[x][y] == 2 and count == 0:
                    self.result += 1