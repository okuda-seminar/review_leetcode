#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        time: O(numRows^2)
        space: O(numRows^2)
        """
        output = [[1]]
        for Row in range(2, numRows + 1):
            cur_Row_list = [1]
            for i in range(1, Row - 1):
                cur_Row_list.append(pre_Row_list[i - 1] + pre_Row_list[i])
            cur_Row_list.append(1)
            pre_Row_list = cur_Row_list
            output.append(cur_Row_list)
        return output

# @lc code=end

