'''
Q[347]. Top K Frequent Elements
'''

# n = len(nums)
# time : O(k * n)
# space : O(n)


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''compute the k most frequent elements
        Args:
            nums(List[int]): array consist of integers (1 <= len(nums) <= 10**5)
            k(int): integer (1 <= k <= the number of unique elements in nums)
        Returns:
            List[int]: the k most frequent elements
        '''
        if not nums:
            raise ValueError('nums should be [1, 10**5]')

        nums_counter = Counter(nums)
        return [nums_counter.most_common()[i][0] for i in range(k)]


# time : O(k * logn)
# space : O(n)

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        nums_counter_list = [(-val, key) for key, val in nums_counter.items()]
        heapq.heapify(nums_counter_list)
        return [heapq.heappop(nums_counter_list)[1] for _ in range(k)]
