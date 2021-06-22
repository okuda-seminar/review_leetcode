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
        """calculate the sum of the squares of digits.

        calculate the square of each digit of num and calculate the sum
        """
        return sum(int(i) ** 2 for i in str(num))
# @lc code=end

