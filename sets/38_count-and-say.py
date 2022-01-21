#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        """Function to convert number to string
        Args:
            n(int): integer
        Returns:
            str: string
        """
        if n == 1:
            return "1"

        nums = self.countAndSay(n - 1)

        count = 1
        ans_list = []
        for idx, num in enumerate(nums):
            if idx != 0 and nums[idx - 1] != num:
                ans_list.append(str(count) + nums[idx - 1])
                count = 1
            elif idx != 0 and nums[idx - 1] == num:
                count += 1

            if idx == len(nums) - 1:
                ans_list.append(str(count) + num)
            
        
        return "".join(ans_list)
# @lc code=end
