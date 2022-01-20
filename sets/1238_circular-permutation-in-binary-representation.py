'''
Q[1238]. Circular Permutation in Binary Representation
'''

# time : O(2**n)
# space : O(2**n)


from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        '''Return any permutation of 2**n
        Args:
            n(int): integer (1 <= n <= 16)
            start(int): the number of start
        Returns:
            List[int]: any permutation of 2**n
        '''
        perm = []
        self.recursion(n, start, perm)
        return perm


    def recursion(self, n: int, binary: int, perm: List[int]) -> int:
        '''Compute permutation of 2**n
        Args:
            n(int): integer
            binary(int): binary representation
            perm(List[int]): permutation of 2**n
        Returns:
            int: binary representation
        '''
        if n == 0:
            perm.append(binary)
            return binary

        binary1 = self.recursion(n - 1, binary ^ 0, perm)
        binary2 = self.recursion(n - 1, binary1 ^ (1 << n - 1), perm)
        return binary2
