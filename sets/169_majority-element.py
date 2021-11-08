'''
Q[169]. Majority Element
'''

# n = len(nums)
# time : O(n)
# space : O(n)

from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''find majority element in nums
        Args:
            nums(List[int]): an array consist of integers (1 <= len(nums) <= 5 * 10**4)
        Returns:
            int: majority element in nums
        '''
        if not nums:
            raise ValueError('nums should be [1, 5 * 10**4]')

        nums_counter = Counter(nums)
        for key, value in nums_counter.items():
            if value > len(nums) // 2:
                return key


# n = len(nums)
# time : O(n)
# space : O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError('nums should be [1, 5 * 10**4]')

        majority_num = num_count = 0

        for num in nums:
            if num_count == 0:
                majority_num = num
                num_count += 1

            if num == majority_num:
                num_count += 1
            else:
                num_count -= 1

        return majority_num
