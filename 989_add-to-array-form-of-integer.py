# n = nums.length
# time = O(n)
# space = O(n)
# done time = 15m


class Solution:

    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        return [int(n) for n in str(int(''.join(map(str, A))) + K)]
