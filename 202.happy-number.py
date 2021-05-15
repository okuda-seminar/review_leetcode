#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        """
        time: O(logn)
        space: O(logn)
        """
        num_list = [n]
        while True:
            n = self.calculate_digit_squares(n)
            if n == 1:
                return True

            elif n in num_list:
                return False

            num_list.append(n)

    def calculate_digit_squares(self, num: int) -> int:
        """
        calculate the sum of the squares of its digits.
        """
        digit_squares = 0
        for i in str(num):
            digit_squares += int(i) ** 2
        return digit_squares
# @lc code=end

