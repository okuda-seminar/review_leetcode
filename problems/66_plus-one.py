# n = digits.length
# time = O(n)
# space = O(n)
# done time = 10m


class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(n) for n in str(int(''.join(map(str, digits))) + 1)]
