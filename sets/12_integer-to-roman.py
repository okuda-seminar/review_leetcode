#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
"""
n: len(str(num))
time: O(n)
space: O(n)
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        """Function to convert integer to Roman
        Args:
            num(int): integer
        Returns:
            str: string
        """
        symbol = "MDCLXVI"
        value = [1000, 500, 100, 50, 10, 5, 1]
        ans = []

        for idx, value_num in enumerate(value):
            if value_num <= num:
                repeat = num // value_num
                if repeat == 4:
                    num = num % value_num
                    if ans and ans[-1] == symbol[idx - 1]:
                        ans[-1] = symbol[idx] + symbol[idx - 2]
                    else: 
                        ans.append(symbol[idx] + symbol[idx - 1])
                else:
                    num = num % value_num
                    ans.append(symbol[idx] * repeat)

        return "".join(ans)
# @lc code=end

