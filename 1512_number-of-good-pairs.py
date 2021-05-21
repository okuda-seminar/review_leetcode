# N = len(nums)
# time: O(N)
# space: O(N)

from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ref = defaultdict(int)
        ret = 0
        for n in nums:
            ret += ref[n]
            ref[n] += 1
        return ret
