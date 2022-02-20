"""
union find
n = number of nodes
m = len(nums)
time = O(mlog n)
space = 0(m)
"""
class Node:
    
    def __init__(self, val):
        self.val = val
        self.parent = self
        self.size = 1

class UnionFind:
        
    def find(self, x):
        if x.parent != x:
            x.parent = self.find(x.parent)
        return x.parent
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            y.parent = x
            x.size += y.size
        return x.size
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """longest consecutive
        Args:
            nums (List[int]): unsorted array of integers
            
        Returns:
            int: length of the longest consecutive element sequences
            
        Examples:
            longestConsecutive([100,2,3,4,1,100]) <- 4
        """
        uf = UnionFind()
        nodes = {}
        max_size = 0
        for num in nums:
            if num not in nodes:
                node = Node(num)
                nodes[num] = node
                size = 1
                if num + 1 in nodes:
                    size = uf.union(node, nodes[num+1])
                    print(1,size,num)
                if num - 1 in nodes:
                    size = uf.union(node, nodes[num-1])
                    print(-1,size,num)
                max_size = max(max_size, size)
                
        return max_size