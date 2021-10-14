# n = length of nums
# time = O(nlogn)
# space = O(n)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Args:
            nums (List[int]): integer array called nums
            k (int): integer called k
        Returns:
            int: kth number in array of nums
        Examples:
            nums = [3,2,5,4,1] k = 2 <- 4
            nums = [1,4,4,3,2,3] k = 4 <- 3
        """
        if k > len(nums):
            raise ValueError("kth number is not existed")
        if len(nums) < 1 or 10**4 < len(nums):
            raise ValueError("nums is out of range")
        nums.sort()
        return nums[-k]