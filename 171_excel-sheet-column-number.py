

#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
        time: O(len(columnTitle))
        space: O(len(columnTitle))
        """
        ref = {}
        for i in range(1, 27):
            ref[chr(64 + i)] = i
        columnTitle_list = list(columnTitle)
        cur_num = 0
        num_alp = 26
        for idx, char in enumerate(columnTitle_list):
            cur_num += ref[char] * (num_alp ** (len(columnTitle_list) - idx - 1))
        return cur_num
# @lc code=end
