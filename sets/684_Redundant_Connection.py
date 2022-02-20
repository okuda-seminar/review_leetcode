"""
UnionFind
n = len(edges)
time = O(nlog n)
space = O(1)
"""
class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * (n + 1)
    
    def find(self, x: int) -> int:
        if self.parent[x] < 0:
            return x
        
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
    def union(self, x: int, y: int) -> None:
        union_x = self.find(x)
        union_y = self.find(y)
        
        if union_x == union_y:
            return True
        
        else:
            self.parent[union_x] = union_y
            return False
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Args:
            edges (List[List[int]]): a tree with n nodes labeled from 1 to n and with one additional edge added
        
        Returns:
            List[int]: an edge that can be removed so that the resulting graph is a tree of n nodes
        """
        uf = UnionFind(len(edges))
        
        for u, v in edges:
            if uf.union(u, v):
                return [u,v]