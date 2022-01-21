#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow1(self, x: float, n: int) -> float:
        """Calculates x raised to the power n

        Args:
            x(float): float
            n: int

        Returns:
            float: x^n
        """
        return pow(x, n)


"""
time complexity : O(log|n|)
space complexity : O(log|n|)
"""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """Calculates x raised to the power n

        Args:
            x(float): float
            n: int

        Returns:
            float: x^n
        """
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n % 2 == 0:
            return self.myPow(x * x, n/2)
        
        return x * self.myPow(x, n-1)
# @lc code=end
