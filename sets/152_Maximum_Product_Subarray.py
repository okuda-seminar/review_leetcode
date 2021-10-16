# n = len(nums)
# time = O(n)
# space = O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Args:
            nums (List[int]): integer array
        Returns:
            int: largest product in contignous non-empty subarray
        Examples:
            maxProduct([2, 4, -3, 5]) <- 8
        """
        assert type(nums) == list, "nums should be list"
        if len(nums) < 1 or 2 * 10**4 < len(nums):
            raise ValueError("length of nums should be one or more and twenty thousand or less")
        for i in range(len(nums)):
            assert type(nums[i]) == int, "nums[i] should be list"
            if nums[i] < -10 or 10 < nums[i]:
                raise ValueError("length of nums[i] is minus ten or more and ten or less")
            curr_num = nums[i]
            if i == 0:
                prev_max = prev_min = ans = curr_num
            else:
                tmp = prev_max
                prev_max = max(curr_num, prev_max * curr_num, prev_min * curr_num)
                prev_min = min(curr_num, tmp * curr_num, prev_min * curr_num)
                ans = max(ans, prev_max)
        return ans