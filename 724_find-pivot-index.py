# n = nums.length
# time = O(n)
# space = O(n)
# done time = 15m


from itertools import accumulate


class Solution:

    def pivotIndex(self, nums: List[int]) -> int:
        cum_sum = list(accumulate(nums))
        if cum_sum[-1] == cum_sum[0]:
            return 0
        nums_sum = cum_sum[-1]
        for i in range(0, len(nums)-1):
            if nums_sum == cum_sum[i]*2 + nums[i+1]:
                return i+1
        return -1
