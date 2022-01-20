'''
Q[797]. 797. All Paths From Source to Target
'''

# n = len(graph)
# time : O(2**n)
# space : O(2**n)


from typing import List


class Solution:

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''Compute all paths from source to target
        Args:
            graph(List[List[int]]): a directed acyclic graph (2 <= len(graph) <= 15)
        Returns:
            List[List[int]]: all paths from source to target
        '''
        if not graph:
            raise ValueError('graph should not be empty.')

        self.graph = graph
        self.all_paths = []
        INIT_PATH = [0]
        INIT_IDX = 0
        self.backtracking(INIT_PATH, INIT_IDX)
        
        return self.all_paths
        
    def backtracking(self, path: List[int], idx: int) -> None:
        '''backtrack 
        path(List[int]): path from source to target
        idx(int): index of graph
        '''
        if idx == len(self.graph) - 1:
            self.all_paths.append(path)
            return None
        
        for val in self.graph[idx]:
            self.backtracking(path + [val], val)
