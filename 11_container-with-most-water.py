#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        time: O(len(height))
        space: O(1)
        """
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right - left) * min(height[right], height[left]))
            if height[right] <= height[left]:
                right -= 1
            else:
                left += 1
        return area
# @lc code=end
