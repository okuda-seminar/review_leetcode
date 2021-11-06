'''
Q[693]. Binary Number with Alternating Bits

n = the number of bits of n
time : O(n)
space : O(n)
'''

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        '''check whether it has alternating bits
        Args:
            n(int): integer
        Returns:
            bool: True if n has alternating bits
        '''
        if not n:
            raise ValueError('n should be [1, 2**31 - 1]')
            
        n_2 = bin(n)[2:]
        for i in range(1, len(n_2)):
            if n_2[i] == n_2[i - 1]:
                return False
            
        return True
    
        #easy solution
        return "00" not in bin(n) and "11" not in bin(n)
