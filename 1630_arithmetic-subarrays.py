# n = nums.length
# m = l.length = r.length <= 500
# time = O(mnlogn)
# space = O(m)


class Solution:

    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            subarray = sorted(nums[l[i]: r[i] + 1])
            diff = subarray[1] - subarray[0]
            res.append(True)

            for k in range(2, len(subarray)):
                if subarray[k] - subarray[k - 1] != diff:
                    res[-1] = False
                    break

        return res
