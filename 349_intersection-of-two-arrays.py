#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        time: O(len(nums1) * len(nums2))
        space: O(n)
        n : min(len(nums1), len(nums2))
        """
        return set(nums1).intersection(set(nums2))
# @lc code=end

