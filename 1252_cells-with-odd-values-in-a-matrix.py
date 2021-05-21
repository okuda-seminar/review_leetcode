from collections import defaultdict
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = defaultdict(int)
        cols = defaultdict(int)
        for r, c in indices:
            rows[r] += 1
            cols[c] += 1
             
        ret = 0
        for r in range(n):
            for c in range(m):
                ret += (rows[r] + cols[c]) % 2
        return ret 
