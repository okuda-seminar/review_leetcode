# n = n
# time = O(n)
# space = O(1)


class Solution:

    def minOperations(self, n: int) -> int:
        res = 0
        half_idx = n // 2
        for i in range(half_idx):
            res += n - (2*i + 1)
        return res
