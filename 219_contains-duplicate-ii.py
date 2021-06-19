# n = nums.length
# time = O(n)
# space = O(n)
# done time = 30m


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums:
            return False

        num_position = {}
        for i, num in enumerate(nums):
            if num in num_position and abs(i - num_position[num]) <= k:
                return True

            num_position[num] = i
        return False
