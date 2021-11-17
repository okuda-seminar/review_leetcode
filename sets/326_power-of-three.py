#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
"""
time complexity: O(logn)
space complexity: O(1)
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """Return True if n is power of 3
        
        Args:
            n(int): integer
        
        Returns:
            bool: return True if n is power of 3
        """
        if n == 1:
            return True

        if n <= 0 or n % 3 != 0:
            return False

        return self.isPowerOfThree(n // 3)



"""
time complexity: O(logn)
space complexity: O(1)
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        """Return True if n is power of 3
        
        Args:
            n(int): integer
        
        Returns:
            bool: return True if n is power of 3
        """
        if n <= 0:
            return False
        
        while n % 3 == 0:
            n = n // 3

        return n == 1
# @lc code=end

