Q[1646]. Get Maximum in Generated Array

time : O(n)
space : O(n)
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        '''compute the maximum integer in nums
        Args:
            n(int): array "nums" length
        Returns:
            int: the maximum integer in nums (nums[2*i] = nums[i], nums[2*i + 1] = nums[i] + nums[i + 1])
        '''
        nums = [0, 1]
        if n <= 1:
            return nums[n]

        for i in range(2, n + 1):
            if i % 2 == 0:
                nums.append(nums[i // 2])
            else:
                nums.append(nums[(i - 1) // 2] + nums[(i - 1) // 2 + 1])

        return max(nums)
