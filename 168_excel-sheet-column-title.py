#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        time: O(x)  x : 26^x < columnNumber < 26^(x + 1)
        space: O(x)
        """
        alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        column_title_list = []
        cur_quotient = columnNumber
        cur_remainder = 0
        while 26 < cur_quotient:
            cur_remainder = cur_quotient % 26
            cur_quotient = (cur_quotient - 1) // 26
            column_title_list.append(alp[cur_remainder - 1])
        column_title_list.append(alp[cur_quotient - 1])
        return ''.join(column_title_list[::-1])

# @lc code=end

