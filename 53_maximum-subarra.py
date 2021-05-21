# n = nums.length
# time = 0(n)
# space = O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ret = max(nums)
        sub_sum = 0
        for num in nums:
            sub_sum = max(0, sub_sum) + num
            ret = max(ret, sub_sum)
        return ret
