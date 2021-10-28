"""
A.1 heap
n = len(mat)
time = O(nlog n)
space = O(n + k)
"""
import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        Args:
            mat (List[List[int]]): m x n binary matrix mat of 1 and 0
            k (int): the number of weakest rows
        Returns:
            List[int]: get index of k weakest rows in mat ordered from weakest to strongest
        Examples:
            kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3) <- [2,0,3]
        """
        mat_list = [[mat[i],i] for i in range(len(mat))]
        return [i for v, i in heapq.nsmallest(k, mat_list)]
"""
A.2 sort
n = len(mat)
time = O(nlog n)
space = O(n)
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        s = [[sum(g),i] for i,g in enumerate(mat)]
        s.sort()
        return [r[1] for r in s[:k]]