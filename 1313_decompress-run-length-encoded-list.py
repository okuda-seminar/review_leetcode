class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ret = []
        i = 0
        while i < len(nums):
            j = 0
            while j < nums[i]:
                ret.append(nums[i+1])
                j += 1
            i += 2
        return ret
