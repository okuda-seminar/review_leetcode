# n = n
# time = O(n)
# space = O(1)
# done time = 20m


class Solution:

    def reinitializePermutation(self, n: int) -> int:
        distinguish_idx = 1
        ans = 0

        while ans == 0 or distinguish_idx != 1:
            distinguish_idx = 2*distinguish_idx
            if distinguish_idx >= n - 1:
                distinguish_idx -= n - 1
            ans += 1

        return ans
