# n = target.length
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:

    def minFlips(self, target: str) -> int:
        flip_count = int(target[0])
        for i in range(1, len(target)):
            if target[i-1] != target[i]:
                flip_count += 1

        return flip_count
