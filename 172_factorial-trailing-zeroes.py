# n = n
# time = O(logn)
# space = O(1)
# done time = 5m


class Solution:

    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        res = 0
        div = 5
        while 1 < n:
            n //= div
            res += n
        return res
