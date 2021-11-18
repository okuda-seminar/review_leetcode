# n = len(nums)
# time = O(n)
# space = O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Args:
            nums (List[int]): array of integers, which got duplicated on one of the duplicated 
        Returns:
            List[int]: repetition of one number and loss of another number
        Examples:
            findErrorNums([1,2,2,4,5]) <- [2,3]
        """
        l, s = len(nums), sum(set(nums))
        l = l * (l + 1) // 2
        return [sum(nums) - s, l - s]