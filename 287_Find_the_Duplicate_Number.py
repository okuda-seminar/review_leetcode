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
        d = {}
        for num in nums:
            if num in d:
                return num

            d[num] = 1

# Floyd's cycle detection algorithm
# n = len(nums)
# time = O(n)
# space = O(1)
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
        slow, fast = nums[0], nums[nums[0]]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break;
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow