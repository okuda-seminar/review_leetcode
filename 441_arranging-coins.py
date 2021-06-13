# n = n
# time = O(logn)
# space = O(1)
# done time = 10m


class Solution:

    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n + 1
        while 1 < high - low:
            mid = (low + high) >> 1
            arithmetic_progression_sum_to_mid = mid*(mid + 1) >> 1

            if arithmetic_progression_sum_to_mid  == n:
                return mid

            if arithmetic_progression_sum_to_mid  < n:
                low = mid
            else:
                high = mid
        return low
