#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        time: O(len(numbers))
        space: O(len(numbers))
        """
        if not numbers:
            return None

        ref = {}
        for idx, n in enumerate(numbers):
            if target - n in ref:
                return [ref[target - n] + 1, idx + 1]
            ref[n] = idx

# @lc code=end

