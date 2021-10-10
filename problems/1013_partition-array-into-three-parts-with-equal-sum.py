#n = arr.length
# time = O(n)
# space = O(1)
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sub_sum, m = divmod(sum(arr), 3)
        if m != 0:
            return False
        sub = 0
        a = 0
        for num in arr:
            sub += num
            if sub == sub_sum:
                sub = 0
                a += 1
        return 2 < a
