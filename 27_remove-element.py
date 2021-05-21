#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        time: O(len(nums))
        space: O(1)
        """
        if not nums:
            return 0
        len_output = 0
        for cur_input in range(len(nums)):
            if nums[cur_input] != val:
                nums[len_output] = nums[cur_input]
                len_output += 1
        return len_output
# @lc code=end

