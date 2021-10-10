# n = nums.length
# time = O(nlogn)
# space = O(1)
# done time = 1h


class Solution:

    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ret1 = nums[-3] * nums[-2] * nums[-1]
        ret2 = nums[0] * nums[1] * nums[-1]
        ret3 = nums[0] * nums[1] * nums[2]
        return max(ret1, ret2, ret3)
