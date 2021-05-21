# n = nums.length
# time = O(nlogn)
# space = O(1)
# done time = 5m


class Solution:

    def dominantIndex(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)
        return nums.index(arr[0]) if len(arr) == 1 or 2 * arr[1] <= arr[0] else -1
