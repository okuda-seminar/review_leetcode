#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """return index in rotated sorted array

        Args:
            nums(List[int]): rotated sorted array
            target(int): integer

        Returns:
            int: return the index of target if it is in nums, or -1 if it is not in nums
        """
        """
        time complexity: O(logn)
        space complexity: O(1)
        """
        if len(nums) == 0:
            return -1

        left = -1
        right = len(nums)
        while 1 < right - left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                if nums[left] < target and nums[mid] < nums[left]:
                    right = mid
                else:
                    left = mid

            else:
                if target <= nums[left] and nums[left] < nums[mid]:
                    left = mid
                else:
                    right = mid

        return -1
# @lc code=end
