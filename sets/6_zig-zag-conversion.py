#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
"""
time: O(n)
space: O(n^2)
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Function to return zig-zag string
        Args:
            s(str): string
            numRows(int): number of rows
        Returns:
            str: zig-zag string
        """
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]

        go_down = True
        row = 0

        for i in range(len(s)):
            rows[row].append(s[i])

            if row == numRows - 1:
                go_down = False
            elif row == 0:
                go_down = True

            if go_down:
                row += 1
            else: 
                row -= 1

        ans_list = ["".join(row_list) for row_list in rows]
        return "".join(ans_list)
# @lc code=end

