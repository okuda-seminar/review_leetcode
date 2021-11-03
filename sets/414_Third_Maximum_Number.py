# n = len(nums)
# time = O(nlogn)
# space = O(1)
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
        nums = list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]
        else:
            return nums[-3]

# n = len(nums)
# time = O(n)
# space = O(1)
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
        three_num = [float('-inf')] * 3
        for num in nums:
            if three_num[2] < num:
                three_num = [three_num[1], three_num[2], num]
            elif three_num[1] < num and three_num[2] != num:
                three_num = [three_num[1], num, three_num[2]]
            elif three_num[0] < num and three_num[2] != num and three_num[1] != num:
                three_num = [num, three_num[1], three_num[2]]
        if three_num[0] == float('-inf'):
            return three_num[2]
            
        return three_num[0]