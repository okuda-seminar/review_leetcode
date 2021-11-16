#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
import bisect


# ans1
"""
n = len(nums)
time complexity: O(logn)
space complexity: O(logn)
"""
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
        left, right = -1, len(self.nums)
        while 1 < right - left:
            mid = (left + right) // 2
            if self.nums[mid] < target:
                left = mid
            else:
                right = mid
        return right


# use bisect
"""
n = len(nums)
time complexity: O(logn)
space complexity: O(1)
"""
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

        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target)

        if left == right:
            return [-1, -1]
        
        return [left, right - 1]
# @lc code=end
