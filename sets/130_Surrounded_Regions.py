"""
union find
n = len(board)
m = len(board[0])
time = O(mn)
space = O(mn)
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Args:
            board (List[List[int]]): m x n matrix containing x and o
        """
        n = len(board)
        m = len(board[0])
        self.surround = {i:i for i in range(n*m+1)}
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    if i in [0, n-1] or j in [0, m-1]:
                        self.surround[i*m+j] = n*m
                    if i - 1 >= 0 and board[i-1][j] == 'O':
                        self.union((i-1)*m+j, i*m+j)
                    if j - 1 >= 0 and board[i][j-1] == 'O':
                        self.union(i*m+j-1, i*m+j)
        for i in range(n):
            for j in range(m):
                if self.find(i*m+j) != n*m:
                    board[i][j] = 'X'
    def find(self, x:int):
        if x != self.surround[x]:
            self.surround[x] = self.find(self.surround[x])
        return self.surround[x]
    
    def union(self, x:int, y:int):
        union_x = self.find(x)
        union_y = self.find(y)
        if union_x > union_y:
            self.surround[union_y] = union_x
        elif union_x < union_y:
            self.surround[union_x] = union_y
"""
dfs
n = len(board)
m = len(board[0])
time = O(mn)
space = O(1)
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        Args:
            board (List[List[int]]): m x n matrix containing x and o
        """
        self.n = len(board)
        self.m = len(board[0])
        self.board = board
        if not self.board or not self.board[0]:
            return []
        for i in [0, self.n-1]:
            for j in range(self.m):
                self.dfs(i, j)   
        for i in range(self.n):
            for j in [0, self.m-1]:
                self.dfs(i, j)
        
        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] == 'O':
                    self.board[i][j] = 'X'
                if self.board[i][j] == 'Z':
                    self.board[i][j] = 'O'
    
    def dfs(self, i:int, j:int):
        if 0 <= i < self.n and 0 <= j < self.m and self.board[i][j] == 'O':
            self.board[i][j] = 'Z'
            self.dfs(i-1,j)
            self.dfs(i+1,j)
            self.dfs(i,j-1)
            self.dfs(i,j+1)