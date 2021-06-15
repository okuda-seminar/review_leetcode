#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        time: O(n^2)
        space: O(1)
        n = len(nums)
        """
        nums.sort()
        min_difference = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum_nums = nums[i] + nums[left] + nums[right]
                diff = abs(sum_nums - target)
                if sum_nums < target:
                    left += 1
                elif sum_nums > target:
                    right -= 1
                else:
                    return target

                if diff < min_difference:
                    min_difference = diff
                    output_sum = sum_nums
                min_difference = min(abs(min_difference), abs(sum_nums - target))

        return output_sum
# @lc code=end
