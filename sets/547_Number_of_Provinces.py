"""
union find
n = length of matrix row
time = O(n^2)
space = O(n^2)
    self.parent:O(n)
    total:O(n)
"""
class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.parent = [0]*n
        for i in range(n):
            self.parent[i] = i
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xlist = self.find(x)
        ylist = self.find(y)
        if xlist != ylist:
            self.parent[ylist] = xlist
    
    def get_count(self):
        total = set()
        for i in range(self.n):
            total.add(self.find(i))
        return len(total)
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """Find circle num
        Args:
            isConnected (List[List[int]]) : 2D matrix wheter ith city and jth city are directly connected
        Returns:
            int: the total number of provinces
        
        Examples:
            findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) -> 3
        """
        n = len(isConnected[0])
        node = UnionFind(n)
        
        for r in range(len(isConnected)):
            for c in range(n):
                if isConnected[r][c] == 1:
                    node.union(r,c)
        
        return node.get_count()