'''
Q[191]. Number of 1 Bits

time : O(n) (n = 32)
space : O(1)
'''


class Solution:
    def hammingWeight(self, n: int) -> int:
        '''count number of 1 bits
        Args:
            n(int): an unsigned integer (len(n) = 32)
        Returns:
            int: number of 1 bits for n
        '''

        num_one_bits = 0
        for i in range(32):
            if (n >> i) & 1:
                num_one_bits += 1
        
        return num_one_bits
