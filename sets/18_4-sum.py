#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
"""
n = len(nums)
time: O(n^3)
space: O(1)
"""
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """Function to return the pair which sum equals to target
        Args:
            nums(List[int]): List of integer
        Returns:
            List[List[int]]: an array of all the unique quadruplets
        """
        if len(nums) < 4:
            return []

        nums.sort()
        ans = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                sum_i_j = nums[i] + nums[j]
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[left] + nums[right] == target - sum_i_j:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                    elif nums[left] + nums[right] < target - sum_i_j:
                        left += 1

                    else: 
                        right -= 1

        return ans
# @lc code=end
