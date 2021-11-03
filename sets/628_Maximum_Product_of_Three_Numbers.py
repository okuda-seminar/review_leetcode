# n = len(nums)
# time = O(nlogn)
# space = O(1)
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
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])

# n = len(nums)
# time = O(n)
# space = O(1)
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
        small_list = [float('inf')] * 2
        large_list = [float('-inf')] * 3
        for num in nums:
            if num <= small_list[0]:
                small_list[0] = num
                small_list.sort(reverse=True)
            if num >= large_list[0]:
                large_list[0] = num
                large_list.sort()
        return max(small_list[0] * small_list[1] * large_list[2], 
                    large_list[0] * large_list[1] * large_list[2])