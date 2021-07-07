# n = nums.length
# time = O(n)
# space = O(n)
# done time  = 10m


from collections import Counter


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_count = Counter(nums).items()
        return [num for num, count in nums_count if count == 2]
