'''
Q[231]. Power of Two
'''

#time : O(logn)
#space : O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        '''Determine whether n is a power of 2
        Args:
            n(int): integer (-2**31 <= n <= 2**31 - 1)
        Returns:
            bool: True if n is a power of 2
        '''
        if n <= 0:
            return False

        div = 2
        while n > 1:
            n, mod = divmod(n, div)
            if mod != 0:
                return False

        return True

#time : O(logn)
#space : O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        if n == 1:
            return True

        div = 2
        n, mod = divmod(n, div)
        if mod != 0:
            return False

        return self.isPowerOfTwo(n)
