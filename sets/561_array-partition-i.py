Q[561]. Array Partition I

n = len(nums)
time : O(nlogn)
space : O(1)

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        '''compute the maximized sum of min(a_i, b_i)
        Args:
            nums(List[int]): array of integers (2 <= len(nums) <= 2 * 10^4)
        Returns:
            int: the maximized sum of min(a_i, b_i) (group array into n pair (a_i, b_i)) 
        '''
        if not nums:
            raise ValueError('nums.length should be [2, 2 * 10^4]')
        
        nums.sort()
        arr_pair_sum = 0
        for i in range(0, len(nums), 2):
            arr_pair_sum += nums[i]
            
        return arr_pair_sum
