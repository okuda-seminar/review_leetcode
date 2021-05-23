# n = nums.length
# time = O(nlogn)
# space = O(1)
# done time = 10m


class Solution:

    def thirdMax(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        sort_nums.reverse()
        max_ordinal_num = 1
        for i in range(1, len(sort_nums)):
            if sort_nums[i] < sort_nums[i-1]:
                max_ordinal_num += 1
                if max_ordinal_num == 3:
                    return sort_nums[i]

        return sort_nums[0]
