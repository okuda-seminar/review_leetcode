# n = len(nums)
# time = O(n)
# space = O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Args:
            nums (List[int]): integer array
        Returns:
            bool: any values appear at least twice
        Examples:
            containsDuplicate([1,2,3,4,1]) <- true
            containsDuplicate([2,3,4,5,6]) <- false
        """
        assert type(nums) == list, "nums should be list"
        if len(nums) < 1 or 10**5 < len(nums):
            raise ValueError("nums length should be one or more and ten thousand or less")
        for num in nums:
            assert type(num) == int, "nums[i] should be integer"
            if num < -10**9 or 10**9 < num:
                raise ValueError("nums[i] length should be -10^9 or more and 10^9 or less")
        return len(set(nums)) != len(nums)






# n = len(nums)
# time = O(n)
# space = O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Args:
            nums (List[int]): integer array
        Returns:
            bool: any values appear at least twice
        Examples:
            containsDuplicate([1,2,3,4,1]) <- true
            containsDuplicate([2,3,4,5,6]) <- false
        """
        assert type(nums) == list, "nums should be list"
        if len(nums) < 1 or 10**5 < len(nums):
            raise ValueError("nums length should be one or more and ten thousand or less")
        d = {}
        for num in nums:
            assert type(num) == int, "nums[i] should be integer"
            if num < -10**9 or 10**9 < num:
                raise ValueError("nums[i] length should be -10^9 or more and 10^9 or less")
            if num in d:
                return True
            else:
                d[num] = 1
        return False