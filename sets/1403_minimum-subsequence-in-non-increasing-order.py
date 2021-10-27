'''
Q[1403]. Minimum Subsequence in Non-Increasing Order

n = len(nums)
time : O(nlogn)
space : O(n)
'''

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        '''compute a subsequence of the array
        Args:
            nums(List[int]): the array consist of integers (1 <= len(nums) <= 500)
        Returns:
            List[int]: a subsequence of the array whose sum of elements is strictly greater than the sum of the non included elements
        '''
        if not nums:
            raise ValueError('len(nums) should be [1, 500]')

        nums.sort()
        ans = []
        sum_nums = sum(nums)
        sum_ans = 0
        while True:
            ans.append(nums[-1])
            sum_ans += nums[-1]
            sum_nums -= nums[-1]
            nums.pop()
            if sum_ans > sum_nums:
                return ans
