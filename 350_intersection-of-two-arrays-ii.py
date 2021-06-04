#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        time: O(len(nums1) * len(nums2))
        space: O(n)
        n : min(len(nums1), len(nums2))
        """
        intersection = []
        for num in nums1:
            if num in nums2:
                intersection.append(num)
                nums2.remove(num)
        return intersection
# @lc code=end

