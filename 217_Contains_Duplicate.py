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
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                return True

            else:
                nums_dict[num] = 1
        return False