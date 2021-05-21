# n = s.length
# time = O(n)
# space = O(1)
# done time = 15m


class Solution:

    def checkRecord(self, s: str) -> bool:
        return not(1 < s.count('A') or 'LLL' in s)
