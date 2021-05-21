# n = A.length
# time = O(n)
# space = O(n)
# done time = 30m

class Solution:

    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = 0
        ret = []
        for a in A:
            num = (num << 1) + a
            ret.append(num % 5 == 0)

        return ret
