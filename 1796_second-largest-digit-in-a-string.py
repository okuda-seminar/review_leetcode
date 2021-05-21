# n = s.length
# time = O(nlogn)
# space = O(n)
class Solution:
    def secondHighest(self, s: str) -> int:
        nums = set(str(num) for num in range(10))
        digits = set(int(c) for c in s if c in nums)
        return -1 if len(digits) <= 1 else sorted(digits, reverse=True)[1]
