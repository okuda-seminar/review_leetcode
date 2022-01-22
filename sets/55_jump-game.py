#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
"""
n = len(nums)
time: O(n^2)
space: O(n)
"""
class Solution:
    def canJump1(self, nums: List[int]) -> bool:
        """Function to calculate the reachability
        Args:
            nums(List[int]): integer array
        Returns:
            bool: true if you can reach the last index, or false otherwise
        """
        dp = [False] * len(nums)
        dp[0] = True
        for idx, num in enumerate(nums):
            if dp[idx] == False:
                return False

            step = 1
            while step <= num and (idx + step) < len(nums):
                dp[idx + step] = True
                step += 1

            if dp[-1] == True:
                return True


"""
n = len(nums)
time: O(n)
space: O(1)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Function to calculate the reachability
        Args:
            nums(List[int]): integer array
        Returns:
            bool: true if you can reach the last index, or false otherwise
        """
        next_step = 0
        for idx, num in enumerate(nums):
            next_step = max(next_step - 1, num)
            if next_step == 0 and idx != len(nums) - 1:
                return False
        
        return True
# @lc code=end
