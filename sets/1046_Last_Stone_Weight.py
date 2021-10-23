"""
n is almost length of stones
time = O(n)
space = O(1)
"""
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Args: 
            stones (List[int]): array of integers (1 <= stones.length <= 30, 1 <= stones[i].length <= 1000)
        Returns:
            int: the smallest possible weight of the left stone
        Examples:
            lastStoneWeight([2,7,4,1,8,1]) <- 1
        """
        stones = [-1 * i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones) * -1
            second = heapq.heappop(stones) * -1
            if first != second and second <= first:
                heapq.heappush(stones, second-first)
        return stones[0] * -1 if len(stones) else 0