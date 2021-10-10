#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        """
        time: O(log(num))
        space: O(1)
        """
        while True:
            sum_digits = 0
            while 0 < num:
                sum_digits += num % 10
                num //= 10

            if sum_digits < 10:
                return sum_digits

            num = sum_digits
# @lc code=end

