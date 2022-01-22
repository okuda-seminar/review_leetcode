"""
n : the length of nums
time complexity : O(n)
space complexity : O(2n)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
			
        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums) - 1)
        dp1[0], dp1[1] = nums[0], max(nums[0], nums[1])
        dp2[0], dp2[1] = nums[1], max(nums[1], nums[2])
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i - 1])
            dp2[i] = max(dp2[i-2] + nums[i + 1], dp2[i - 1])
        return max(dp1[-1], dp2[-1])


"""
n : the length of nums
time complexity : O(2n)
space complexity : O(n)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
        
        return max(self.dp(nums[:-1]), self.dp(nums[1:]))
    
    def dp(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]