'''
Q[1863]. Sum of All Subset XOR Totals
'''

# n = len(nums)
# time : O(n!)
# space : O(n)


from collections import deque


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        '''compute the sum of all xor totals for every subset of nums
        Args:
            nums(List(int)): array consist of integers (1 <= len(nums) <= 12)
        Returns:
            int: the sum of all xor totals for every subset of nums
        '''
        if not nums:
            raise ValueError('nums should be [1 12]')

        xor_total = 0
        stack = deque([(0, 0)])

        while stack:
            element_length, cur_xor = stack.pop()
            xor_total += cur_xor

            for i in range(element_length, len(nums)):
                stack.append((i + 1, cur_xor ^ nums[i]))

        return xor_total
