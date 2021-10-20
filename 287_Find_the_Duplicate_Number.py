# n = len(nums)
# time = O(n)
# space = O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """compute finding duplicate number
        Args:
            nums (List[int]): an array of integers in the range [1,n] inclusive
        Returns:
            int: one repeated number
        Examples:
            findDuplicate([1,2,3,4,5,5]) <- 5
        """
        assert type(nums)==list, "type of nums should be list"
        if not nums:
            raise ValueError("nums should be existed")
        d = {}
        for i in nums:
            assert type(i)==int, "type of nums[i] should be integer"
            if i in d:
                return i
            d[i] = 1