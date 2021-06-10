#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
import collections


# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        time: O(len(nums))
        space: O(len(nums))
        """
        nums_counter = collections.Counter(nums)
        disappeared_num = []
        for i in range(1, len(nums) + 1):
            if nums_counter[i] == 0:
                disappeared_num.append(i)
        return disappeared_num
# @lc code=end
