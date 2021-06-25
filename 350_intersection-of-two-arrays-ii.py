#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use intersection
        """
        time: O(len(nums1) * len(nums2))
        space: O(n)
        n : min(len(nums1), len(nums2))

        intersection = []
        for num in nums1:
            if num in nums2:
                intersection.append(num)
                nums2.remove(num)
        return intersection
        """

        # use sort
        """
        time: O(max(n1log(n1), n2log(n2), n1 + n2))
        space: O(n)
        n1 = len(nums1)
        n2 = len(nums2)
        """
        nums1.sort()
        nums2.sort()
        nums1_idx = 0
        nums2_idx = 0
        intersection = []
        while nums1_idx < len(nums1) and nums2_idx < len(nums2):
            if nums1[nums1_idx] == nums2[nums2_idx]:
                intersection.append(nums1[nums1_idx])
                nums1_idx += 1
                nums2_idx += 1
            elif nums1[nums1_idx] < nums2[nums2_idx]:
                nums1_idx += 1
            else:
                nums2_idx += 1
        return intersection
# @lc code=end
