"""
A1.counter
n = len(nums)
time = O(n)
space = O(n)
"""
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value, count = zip(*Counter(nums).most_common())
        return value[:k]

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        value = Counter(nums).most_common(k)
        return [x for x,_ in value]

"""
A2 heap
n = len(nums)
time = O(n)
space = O(n)
"""
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        return heapq.nlargest(k,c,c.get)