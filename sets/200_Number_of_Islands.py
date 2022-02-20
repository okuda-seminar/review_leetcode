"""
union find
n = len(grid)
m = len(grid[0])
time = O(nm)
space = O(nm)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        self.surround = {i:i for i in range(m * n)}
        self.count = sum(grid[i][j]=='1' for i in range(n) for j in range(m))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    if i + 1 <= n - 1 and grid[i+1][j] == "1":
                        self.union((i+1)*m+j,i*m+j)
                    if j + 1 <= m - 1 and grid[i][j+1] == "1":
                        self.union(i*m+j+1,i*m+j)
        
        return self.count
        
    def find(self, x: int):
        if self.surround[x] != x:
            self.surround[x] = self.find(self.surround[x])
        return self.surround[x]
    
    def union(self, x: int, y: int):
        union_x = self.find(x)
        union_y = self.find(y)
        if union_x == union_y:
            return None
        
        self.surround[union_x] = union_y
        self.count -= 1

"""
dfs
n = len(grid)
m = len(grid[0])
time = O(nm)
space = O(1)
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        n = len(grid)
        m = len(grid[0])
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
            
        return count
    
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return None
        grid[i][j] = "#"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

"""
bfs
n = len(grid)
m = len(grid[0])
time = O(nm)
space = O(1)
"""
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    cnt += 1
                    self.bfs(grid, i, j)
        return cnt
    
    def bfs(self, grid: List[List[int]], i: int, j:int) -> None:
        queue = deque([(i,j)])
        while queue:
            I,J = queue.popleft()
            for i,j in [I+1,J],[I,J+1],[I-1,J],[I,J-1]:
                if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue.append((i,j))
        