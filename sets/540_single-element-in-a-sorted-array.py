#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """return single non duplicate element

        Args:
            nums(List[int]): sorted array

        Returns:
            int: the single element that appears only once
        """
        # ans 1
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        """
        if len(nums) == 0 or 10**5 < len(nums):
            raise ValueError("nums length should be one or more and ten thousand or less")

        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                print(i)
                return nums[i]

        return nums[-1]
        """

        # ans 2 (use binary search)
        """
        time complexity: O(log n)
        space complexity: O(1)
        """
        if len(nums) == 0 or 10**5 < len(nums):
            raise ValueError("nums length should be one or more and ten thousand or less")

        left = 0
        right = len(nums) - 1

        while 0 < right - left:
            mid = (right + left) // 2
            if nums[mid - 1] != nums[mid] != nums[mid + 1]:
                return nums[mid]

            if mid % 2 == 0 and nums[mid - 1] == nums[mid]:
                right = mid - 2
            elif mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                left = mid + 2
            elif mid % 2 == 1 and nums[mid - 1] == nums[mid]:
                left = mid + 1
            elif mid % 2 == 1 and nums[mid] == nums[mid + 1]:
                right = mid - 1

        return nums[left]
# @lc code=end
