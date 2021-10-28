# n = len(nums) + 1
# time = O(n)
# space = O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Conputer missing number
        Args:
            nums (List[int]): list of the distinct numbers
        Returns:
            int: missing number from nums
        Examples:
            nums = [1,3,2,0] <- 4
            nums = [1,2,3] <- 0
        """
        if len(nums) < 1 or 10**4 < len(nums):
            raise ValueError("nums length is out of range")
        for i in nums:
            if i < 0 or len(nums) < i:
                raise ValueError("nums[i] is out of range")
        nums_max = max(nums) + 1
        if not list(set(range(nums_max)) - set(nums)):
            return nums_max

        else:
            return list(set(range(nums_max)) - set(nums))[0]


# n = len(nums) + 1
# time = O(n)
# space = O(n)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Conputer missing number
        Args:
            nums (List[int]): list of the distinct numbers
        Returns:
            int: missing number from nums
        Examples:
            nums = [1,3,2,0] <- 4
            nums = [1,2,3] <- 0
        """
        if len(nums) < 1 or 10**4 < len(nums):
            raise ValueError("nums length is out of range")
        for i in nums:
            if i < 0 or len(nums) < i:
                raise ValueError("nums[i] is out of range")
        nums_max = max(nums) + 1
        num_list = list(range(0, nums_max))
        d = {}
        for i in num_list:
            d[i] = 1
        for i in nums:
            if i in d:
                d[i] = 0
        for k,v in d.items():
            if v != 0:
                return k
                
        return nums_max
        