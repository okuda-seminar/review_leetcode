# n = piles.;ength
# time = O(nlogn)
# space = O(1)
# done time = 5m


class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles)//3 : len(piles) : 2])
