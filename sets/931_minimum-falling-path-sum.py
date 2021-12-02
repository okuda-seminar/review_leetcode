'''
Q[931].Minimum Falling Path Sum
'''

# n = len(matrix)
# time : O(n**3)
# space : O(n)


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''Return the minimum sum of path
        Args:
            matrix(List[List[int]]): 2D array of integers (1 <= len(matrix) = len(matrix[i]) <= 100)
        Returns:
            int: the minimum sum of path
        '''
        if not matrix:
            raise ValueError('matrix length should be [1, 100]')

        if len(matrix) != len(matrix[0]):
            raise ValueError('matrix length should be the same as matrix[0]')

        row = matrix[0]
        COL_LENGTH = len(matrix[0])

        for i in range(1, len(matrix)):
            row = [matrix[i][j] + min(row[max(0, j - 1):min(COL_LENGTH, j + 2)]) for j in range(COL_LENGTH)]
        return min(row)
