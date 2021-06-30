

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
        ref = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26, }
        columnTitle_list = list(columnTitle)
        cur_num = 0
        for idx, char in enumerate(columnTitle_list):
            cur_num += ref[char] * (26 ** (len(columnTitle_list) - idx - 1))
        return cur_num
# @lc code=end

