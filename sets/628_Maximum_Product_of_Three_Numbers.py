# n = len(nums)
# time = O(nlogn)
# space = O(n)
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        """
        Args:
            nums (List[int]): integer array (3 <= nums.length <= 10^4, -1000 <= nums[i].length <= 1000)
        Returns:
            int: maximum product
        Examples:
            nums = [1,2,3] <- 6
        """
        assert type(nums) == list, "nums is list"
        if len(nums) < 3 or 10**4 < len(nums):
            raise ValueError("nums is out of range")
        for i in nums:
            assert type(i) == int, "nums[i] is integer"
            if i < -1000 or 1000 < i:
                raise ValueError("nums[i] is out of range")
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])