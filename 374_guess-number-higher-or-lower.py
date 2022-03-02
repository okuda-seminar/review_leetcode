# n = n
# time = O(logn)
# space = O(1)
# done time = 20m


class Solution:

    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n

        left = 0
        right = n + 1

        while 1 < right - left:
            mid = left + right >> 1
            comp = guess(mid)

            if comp == 0:
                return mid

            if 0 < comp:
                left = mid
            else:
                right = mid

        return left
