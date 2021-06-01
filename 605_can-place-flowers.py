# n = flowerbed.length
# time = O(n)
# space = O(1)
# done time = 20m


class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        not_planted_num = 1
        for flower in flowerbed:
            if flower != 0:
                not_planted_num = 0
            else:
                not_planted_num += 1

            if not_planted_num == 3:
                not_planted_num = 1
                n -= 1
        return n <= 1 if not_planted_num == 2 else n <= 0
