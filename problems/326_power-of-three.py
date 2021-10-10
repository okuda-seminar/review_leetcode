# n = n
# time = O(n)
# sapce = O(1)
# done time = 5m


class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        MOD = 3
        while n > 1:
            n, mod = divmod(n, MOD)
            if mod != 0:
                return False

        return True
