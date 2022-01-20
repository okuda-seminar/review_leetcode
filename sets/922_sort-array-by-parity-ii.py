'''
Q[922]. Sort Array By Parity II

n = len(nums)
time : O(n)
space : O(n)
'''

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        '''Sort the array
        Args:
            nums(List[int]): an array of integers (2 <= len(nums) <= 2 * 10^4)
        Returns:
            List[int]: i is odd whenever nums[i] is odd, i is even whenever i is even
        '''
        if not nums:
            return []

        sort_array = [0] * len(nums)
        even_idx = 0
        odd_idx = 1
        for num in nums:
            if num % 2 == 0:
                sort_array[even_idx] = num
                even_idx += 2
            else:
                sort_array[odd_idx] = num
                odd_idx += 2

        return sort_array
