"""
n : the length of nums
time complexity = O(n)
space complexity = O(1)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        elif len(nums) < 3:
            return max(nums)
        
        nums[2] += nums[0]
        for i in range(3, len(nums)):
            nums[i] += max(nums[i - 3], nums[i - 2])
        return max(nums[-1],nums[-2])


"""
n : the length of nums
time complexity = O(n)
space complexity = O(n)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
			
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2]+nums[i], dp[i - 1])
        return dp[-1]