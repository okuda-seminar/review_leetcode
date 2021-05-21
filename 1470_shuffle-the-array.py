class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ret = []
        l = 0
        for i in range(len(nums)):
            if i%2 == 0:
                ret.append(nums[l])
                l += n
            else:
                ret.append(nums[l])
                l -= n-1
        return ret
