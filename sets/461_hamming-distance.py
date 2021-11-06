'''
Q[235]. 461. Hamming Distance
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''compute hamming distance
        Args:
            x(int): integer (0 <= x <= 2**31 - 1)
            y(int): integer (0 <= x <= 2**31 - 1)
        Returns:
            int: hamming distance
        '''
        if x < 0 or y < 0:
            raise ValueError('x, y should be [0, 2**31 - 1]')
        
        #A1
        #n = (length of bits for x(y))
        #time : O(n) 
        #space : O(1)
        return bin(x ^ y).count('1')

        #A2
        #n = (length of bits for x(y))
        #time : O(n) 
        #space : O(1)
        hamming_distance = 0
        while x or y:
            hamming_distance += (x % 2) ^ (y % 2)
            x //= 2
            y //= 2
            
        return hamming_distance
