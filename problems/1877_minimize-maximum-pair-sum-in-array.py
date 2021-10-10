# n = nums.length
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:

    def minPairSum(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        max_sum = sort_nums[0] + sort_nums[-1]
        left = 1
        right = len(nums) - 2

        while left < right:
            max_sum = max(max_sum, sort_nums[left] + sort_nums[right])
            left += 1
            right -= 1

        return max_sum
