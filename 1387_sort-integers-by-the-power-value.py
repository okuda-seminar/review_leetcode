# n = hi - lo
# time = O(nlogn)
# space = O(n)
# done time = 30m


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        memorization = {1: 0}

        def power(x: int) -> int:
            if x in memorization:
                return memorization[x]

            memorization[x] = 1 + power(3*x + 1 if x & 1 else x >> 1)
            return memorization[x]

        power_arr = [(power(x), x) for x in range(lo, hi + 1)]
        return sorted(power_arr)[k - 1][1]
