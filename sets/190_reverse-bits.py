'''
Q[190]. Reverse Bits

n = bit length of n (=32)
time : O(n)
space : O(1)
'''

class Solution:
    def reverseBits(self, n: int) -> int:
        '''reverse bit of n
        Args:
            n(int): integer
        Returns:
            int: reverse bit of n
        '''
        bit_length = 32
        n_bin = bin(n)
        n_bin_zero_pad = '0'*(bit_length - len(n_bin) + 2) + n_bin[2:]
        return int('0b' + n_bin_zero_pad[::-1], 2)
