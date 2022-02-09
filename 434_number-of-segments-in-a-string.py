# n = s.length
# time = O(n)
# space = O(1)
# done time = 15m


class Solution:

    def countSegments(self, s: str) -> int:
        return sum(s[i] != ' ' and (i == 0 or s[i - 1] == ' ')
                   for i in range(len(s)))
