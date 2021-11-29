"""
union find
n = row length of grid
m = column length of grid
time = O(nm)
space = O(nm)
"""
class Solution:
    def maxAreaOfIsland(self, grid:List[List[int]]) -> int:
        """Max area of island
        Args:
            grid (List[List[int]]): n * m array consist of 0 or 1 values
        Return:
            int: size of the maximum island
        """
        n = len(grid)
        m = len(grid[0])
        self.parent = {i:i for i in range(n*m)}
        self.area = {i:1 for i in range(n*m)}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i + 1 <= n - 1 and grid[i+1][j] == 1:
                        self.union(i*m+j, (i+1)*m+j)
                    if j + 1 <= m - 1 and grid[i][j+1] == 1:
                        self.union(i*m+j, i*m+j+1)
                else:
                    self.area[i*m+j] = 0
        return max(self.area.values())

    def find(self, x: int) -> int:
        """find class number
        Args:
            x (int) : element in grid
        Returns:
            int: class number of the element
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y:int):
        """union class number
        Args:
            x (int): element in grid
            y (int): element in grid
        """
        union_x = self.find(x)
        union_y = self.find(y)
        if union_x != union_y:
            self.parent[union_y] = union_x
            self.area[union_x] += self.area[union_y]

