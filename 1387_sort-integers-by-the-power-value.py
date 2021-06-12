# n = hi - lo
# time = O(nlogn)
# space = O(n)
# done time = 30m


class Solution:

    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = [i for i in range(lo, hi+1)]
        power_arr = []

        for num in arr:
            step = 0
            cur_num = num

            while cur_num > 1:
                if cur_num%2 == 0:
                    cur_num /= 2
                else:
                    cur_num = cur_num*3 + 1
                step += 1
            power_arr.append((step, num))

        return sorted(power_arr)[k-1][1]
