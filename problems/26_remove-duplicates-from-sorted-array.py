# O(n) solution in leetcode
# n = nums.length
# time = O(n)
# space = O(1)


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        match_idx = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[match_idx]:
                match_idx += 1
                nums[match_idx] = nums[j]
        return match_idx + 1
