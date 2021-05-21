class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [2*i+start for i in range(n)]
        ret = nums[0]
        for i in range(n-1):
            ret = ret ^ nums[i+1]
        return ret
