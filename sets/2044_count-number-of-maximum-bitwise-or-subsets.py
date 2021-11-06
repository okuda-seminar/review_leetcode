'''
Q[2034]. Count Number of Maximum Bitwise-OR Subsets
'''

# n = len(nums)
# time : O(2**n * n) (n = 16)
# space : O(n)

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        '''compute number of maximum bitwise-OR subsets
        Args:
            nums(List[int]): array consist of integers (1 <= len(nums) <= 16, 1 <= nums[i] <= 10**5)
        Returns:
            int: number of maximum bitwise-OR subsets
        '''
        if not nums:
            raise ValueError('nums length should be [1, 16]')

        max_bitwise_or = 0
        for i in range(len(nums)):
            max_bitwise_or |= nums[i]

        count_max_or_subset = 0
        for i in range(1, 1 << len(nums)):
            num_arr = []
            for j in range(len(nums)):
                if i >> j & 1:
                    num_arr.append(nums[j])

            or_num = 0
            for num in num_arr:
                or_num |= num
            if or_num >= max_bitwise_or:
                count_max_or_subset += 1

        return count_max_or_subset


# n = len(nums)
# time : O(n! * n) (n = 16)
# space : O(n)
from collections import deque


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        stack = deque([])

        for i in range(len(nums)):
            stack.append((nums[i], i))

        max_bitwise_or = 0
        count_max_or_subset = 0

        while stack:
            cur_bitwise_or, idx = stack.popleft()

            if cur_bitwise_or > max_bitwise_or:
                max_bitwise_or = cur_bitwise_or
                count_max_or_subset = 1

            elif cur_bitwise_or == max_bitwise_or:
                count_max_or_subset += 1

            for i in range(idx + 1, len(nums)):
                stack.append((cur_bitwise_or | nums[i], i))

        return count_max_or_subset
