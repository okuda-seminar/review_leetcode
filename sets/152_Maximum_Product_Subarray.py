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
        for i in range(len(nums)):
            curr_num = nums[i]
            if i == 0:
                prev_max = prev_min = ans = curr_num
            else:
                tmp = prev_max
                prev_max = max(curr_num, prev_max * curr_num, prev_min * curr_num)
                prev_min = min(curr_num, tmp * curr_num, prev_min * curr_num)
                ans = max(ans, prev_max)
        return ans