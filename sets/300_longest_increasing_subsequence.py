"""
Q. DP
n = length of nums
time = O(n^2)
space = O(n)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """length of Longest Increasing Subsequence
        Args:
            nums (List[int]): an integer array
        Returns:
            int: the length of the longest strictly increasing subsequence
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            max_len = 0
            for j in range(i-1,-1,-1):
                if nums[j] < nums[i]:
                    max_len = max(max_len, dp[j])
            dp[i] = max_len + 1
        return max(dp)


"""
Q. DP + Binary Search
n = length of nums
time = O(nlog n)
space = O(n)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """length of Longest Increasing Subsequence
        Args:
            nums (List[int]): an integer array
        Returns:
            int: the length of the longest strictly increasing subsequence
        """
        dp = []
        for i in range(len(nums)):
            if not dp or nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                pos = bisect.bisect_left(dp, nums[i])
                dp[pos] = nums[i]
        return len(dp)