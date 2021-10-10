# n = x
# time = O(logn)
# space = O(1)
# done time = 10m


class Solution:

    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        sqrt_num = 0
        while 1 < right - left:
            mid = (left + right) >> 1

            if mid ** 2 <= x:
                sqrt_num = mid
                left = mid
            else:
                right = mid

        return sqrt_num
