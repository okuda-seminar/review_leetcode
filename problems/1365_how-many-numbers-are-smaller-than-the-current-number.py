class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_copy = nums.copy()
        ret = []
        count = 0
        for i in range(len(nums)):
            nums.pop(i)
            nums.insert(0, nums_copy[i])
            count = 0
            j = 1
            while j < len(nums) :
                if nums[0] > nums[j]:
                    count += 1
                j += 1
            ret.append(count)
        return ret
