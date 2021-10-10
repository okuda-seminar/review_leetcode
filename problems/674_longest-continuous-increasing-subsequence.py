# n = nums.length
# time = O(n)
# space = O(1)
# done time = 15m


class Solution:

    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        continuous_count = 1
        max_continuous_count = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                continuous_count += 1
            else:
                max_continuous_count = max(max_continuous_count, continuous_count)
                continuous_count = 1
        max_continuous_count = max(max_continuous_count, continuous_count)
        return max_continuous_count
