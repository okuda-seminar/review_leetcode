# n = nums.length
# time = O(n)
# space = O(k)
# done time = 30m


class Solution:

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sub_sum = sub_sum = sum(nums[:k])
        for i in range(k, len(nums)):
            sub_sum += nums[i] - nums[i - k]
            max_sub_sum = max(max_sub_sum, sub_sum)
        return max_sub_sum / k
