# n = n
# time = O(logn)
# space = O(1)
# done time = 10m


class Solution:

    def arrangeCoins(self, n: int) -> int:
        low = 1
        high = n + 1
        res = 0
        while low < high:
            mid = (low + high) >> 1
            arithmetic_progression_sum_to_mid = mid*(mid + 1) >> 1

            if arithmetic_progression_sum_to_mid  == n:
                return mid

            if arithmetic_progression_sum_to_mid  < n:
                res = mid
                low = mid + 1
            else:
                high = mid
        return res
