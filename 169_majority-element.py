#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
import collections


# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use dict
        """
        time: O(len(nums))
        space: O(len(nums))

        if not nums:
            return None

        ref = {}
        for num in nums:
            if num in ref:
                ref[num] += 1
            else:
                ref[num] = 1
            if (len(nums) / 2) <= ref[num]:
                return num

        return None
        """

        # use collections.Counter
        """
        time: O(N)
        space: O(N)

        count_elements = collections.Counter(nums).most_common()
        if (len(nums) / 2) <= count_elements[0][1]:
            return count_elements[0][0]

        return False
        """

        # use sorting
        """
        time: O(NlogN)
        space: O(1)
        """
        if len(nums) == 1:
            return nums[0]

        nums.sort()
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
                if (len(nums) / 2) <= count:
                    return nums[i]

            else:
                count = 1
        return False

# @lc code=end

