# n = nums.length
# time = O(n)
# space = O(n)
# done time = 30m


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_dict = {}
        for i, num in enumerate(nums):
            if i - nums_dict.get(num, -float('inf')) <= k:
                return True

            else:
                nums_dict[num] = i

        return False
