#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None

        pre_num = start_num = nums[0]
        summary_ranges = []
        for i in range(1, len(nums)):
            if pre_num + 1 != nums[i]:
                if start_num == pre_num:
                    summary_ranges.append(str(pre_num))
                else:
                    summary_ranges.append(str(start_num)+"->"+str(pre_num))
                start_num = nums[i]
            pre_num = nums[i]
        if pre_num == start_num:
            summary_ranges.append(str(pre_num))
        else:
            summary_ranges.append(str(start_num)+"->"+str(pre_num))
        return summary_ranges
# @lc code=end

