#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        time: O(n^2)
        space: O(n)
        n = len(nums)
        """
        nums.sort()
        output_3_nums = []
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    cur_3_nums = [nums[i], nums[left], nums[right]]
                    left += 1
                    right -= 1
                    if output_3_nums and cur_3_nums == output_3_nums[-1]:
                        continue
                    output_3_nums.append(cur_3_nums)

        return output_3_nums
# @lc code=end
