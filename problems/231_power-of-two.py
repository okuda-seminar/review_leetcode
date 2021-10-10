# n = n
# time = O(logn)
# space = O(1)
# done time = 15m


class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        MOD = 2
        while 1 < n:
            n, mod = divmod(n, MOD)
            if mod != 0:
                return False

        return True
