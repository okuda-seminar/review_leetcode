"""
UnionFind
n = len(graph)
m = len(graph[i]) for i in range(n)
time = O(nm)
space = O(nm)
"""
class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, i: int, graph:List[List[int]]):
        if graph:
            root_i = self.find(i)
            root_j = self.find(graph[0])
            if root_i == root_j:
                return True

            for k in range(1, len(graph)):
                root_k = self.find(graph[k])
                if root_i == root_k:
                    return True

                self.parent[root_k] = root_j
        return False
            
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """is bipartite
        Args:
            graph (List[List[int]]) : 2D array graph where graph[u] is an array of nodes that node u is adjacent to.
        Returns:
            bool: whehter a graph is bipartite
        """
        if not graph:
            return False
        
        uf = UnionFind(len(graph))
        for i in range(len(graph)):
            n = len(graph[i])
            
            if uf.union(i, graph[i]):
                return False
            
        return True
"""
DFS (stack)
n = len(graph)
m = len(graph[i]) for i in range(n)
time = O(nm)
space = O(nm)
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for from_node in range(len(graph)):
            if from_node in colors:
                continue
            
            stack = [from_node]
            colors[from_node] = 1
            
            while stack:
                from_node = stack.pop()
                for to_node in graph[from_node]:
                    if to_node in colors:
                        if colors[to_node] == colors[from_node]:
                            return False
                    
                    else:
                        stack.append(to_node)
                        colors[to_node] = colors[from_node]
        return True
"""
DFS 
n = len(graph)
m = len(graph[i]) for i in range(n)
time = O(nm)
space = O(nm)
"""
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}
        for node_from in range(len(graph)):
            if node_from not in colors and not self.dfs(graph, node_from, colors, 1):
                return False

        return True

    def dfs(self, graph, node, colors, color):

        colors[node] = color

        for node_to in graph[node]:
            if node_to in colors:
                if colors[node_to] == colors[node]:
                    return False
            else:
                if not self.dfs(graph, node_to, colors, color * -1):
                    return False

        return True
"""
BFS (queue)
m = len(graph[i]) for i in range(n)
time = O(nm)
space = O(nm)
"""
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        for from_node in range(len(graph)):
            if from_node in colors:
                continue
            
            queue = deque([from_node])
            colors[from_node] = 1 
            
            while queue:
                from_node = queue.popleft()
                for to_node in graph[from_node]:
                    if to_node in colors:
                        if colors[to_node] == colors[from_node]:
                            return False
                    else:
                        queue.append(to_node)
                        colors[to_node] = colors[from_node] * -1

        return True
