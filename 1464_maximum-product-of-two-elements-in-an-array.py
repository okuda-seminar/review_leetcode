class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ret = sorted(nums[:2])
        for n in nums[2:]:
            if n <= ret[0]:
                continue
            if n <= ret[1]:
                ret[0] = n
            else:
                ret[0] = ret[1]
                ret[1] = n
        return (ret[0] - 1) * (ret[1] - 1)
