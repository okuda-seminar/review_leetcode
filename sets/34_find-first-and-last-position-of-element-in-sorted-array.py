#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """ find position

        Args:
            nums(List[int]): list which is sorted in ascending order
            target: integer

        Returns:
            List[int]: starting and ending position of a given target value
        """
        if len(nums) == 0:
            return [-1, -1]

        self.nums = nums
        left_indx = self.search(target)
        right_indx = self.search(target + 1) - 1
        if left_indx <= right_indx:
            return [left_indx, right_indx]

        return [-1, -1]

    def search(self, target):
        left, right = 0, len(self.nums)
        while left < right:
            mid = (left + right) // 2
            if self.nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end
