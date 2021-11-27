'''
Q[821]. Shortest Distance to a Character
'''


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        '''compute the distance between s[i] and c
        Args:
            s(str): string consist of lowercase (1 <= len(s) <= 10^4)
            c(str): standard string
        Returns:
            List[int]: the distance between s[i] and c
        '''
        if not s or not c:
            return []

        standard_idx = []
        for i in range(len(s)):
            if s[i] == c:
                standard_idx.append(i)
        
        # n = len(s)
        # time : O(n^2)
        # space : O(n)
        shortest_to_char = []
        for i in range(len(s)):
            shortest_to_char.append(min([abs(i - j) for j in standard_idx]))

        return shortest_to_char

        # n = len(s)
        # time : O(n)
        # space : O(n)
        shortest_to_char = [0] * len(s)
        idx = 0
        for i in range(len(s)):
            if i < standard_idx[0]:
                shortest_to_char[i] = standard_idx[0] - i
            elif i > standard_idx[-1]:
                shortest_to_char[i] = i - standard_idx[-1]
            elif i == standard_idx[idx]:
                idx += 1
            else:
                shortest_to_char[i] = min(standard_idx[idx] - i, i - standard_idx[idx - 1])
        return shortest_to_char


# n = len(grid)
# m = len(grid[i])
# time : O(n * m)
# space : O((n * m)**2)


from copy import deepcopy


class Solution:

    def __init__(self, grid: list):
        '''Initialize
        Args:
            grid(List[List[str]]): the array consist of strings
        '''
        self.grid = grid
        self.shortest_to_char = [[float('inf')] * len(self.grid[0]) for i in range(len(self.grid))]

    def shortestToChar2(self, c: str) -> list:
        '''Compute the distance between grid[i][j] and c
        Args:
            c(str): standard string
        Returns:
            List[List[int]]: the distance between s[i] and c
        '''
        if not grid:
            return []

        grid_copy = deepcopy(self.grid)

        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == c:
                    self.shortest_to_char[i][j] = 0
                    self.i = i
                    self.j = j
                    self.dfs(i, j)
                    self.grid = deepcopy(grid_copy)

        return self.shortest_to_char

    def dfs(self, i: int, j: int) -> None:
        '''
        Args:
            i(int): the index of grid
            j(int): the index of grid
        '''
        if i < 0 or j < 0 or i >= len(self.grid) or j >= len(self.grid[0]):
            return None

        if self.grid[i][j] is not "visited":
            self.shortest_to_char[i][j] = min(abs(self.i - i) + abs(self.j - j), self.shortest_to_char[i][j])
            self.grid[i][j] = "visited"
            self.dfs(i, j + 1)
            self.dfs(i, j - 1)
            self.dfs(i + 1, j)
            self.dfs(i - 1, j)
