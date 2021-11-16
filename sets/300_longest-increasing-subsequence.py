#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
from bisect import bisect_left


# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """return longest increasing subsequence

        Args:
            nums(List[int]): integer array
        
        Returns:
            int: length of the longest strictly increasing subsequence
        """
        # use binary search
        """
        n = len(nums)
        time complexity: O(nlogn)
        space complexity: O(n)
        """
        """
        def binary_search(arr, num) -> int:
            left = 0
            right = len(arr) - 1
            while left < right:
                mid = (left + right) // 2
                if arr[mid] < num:
                    left = mid + 1
                else: 
                    right = mid
            return left

        arr = []
        for num in nums:
            if not arr or arr[-1] < num:
                arr.append(num)
            else:
                left = binary_search(arr, num)
                arr[left] = num
        return len(arr)
        """


        # use binary search by using bisect
        """
        n = len(nums)
        time complexity: O(nlogn)
        space complexity: O(n)
        """
        arr = []
        for num in nums:
            if not arr or arr[-1] < num:
                arr.append(num)
            else:
                left = bisect_left(arr, num)
                arr[left] = num
        return len(arr)


        # use dp
        """
        n = len(nums)
        time complexity: O(n^2)
        space complexity: O(n)
        """
        """
        if len(nums) == 0:
            return 0

        LIS = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[j] + 1, LIS[i])
        return max(LIS)
        """
# @lc code=end
