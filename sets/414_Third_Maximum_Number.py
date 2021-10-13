# n = len(nums)
# time = O(nlogn)
# space = O(n)
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """Compute third of distinct maximum number
        Args:
            nums (List[int]): array of number
        Returns:
            int: third distinct maximum number
        Examples:
            nums = [1,2,3] <- 1
            nums = [1,2] <- 2
        """
        if len(nums) < 0 or 10**4 < len(nums):
            raise ValueError("nums length is out of range")
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]