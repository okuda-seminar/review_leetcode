# n = 3:
# time = O(nlogn)
# space = O(n)
# done time = 30m


class Solution:

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        if c - a == 2:
            return [0, 0]

        elif min(c - b, b - a) <= 2:
            return [1, c - a - 2]

        return [2, c - a - 2]
