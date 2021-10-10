# n = nums.length
# time = O(nlogn)
# space = O(n)
# done time = 10m


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        set_nums = list(set(nums))
        if len(set_nums) < 3:
            return max(nums)

        return sorted(set_nums)[-3]
