'''
Q[119]. Pascals Triangle II


n = rowIndex ([1, 33])
time : O(n^2)
space : O(n)
'''

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''Compute rowIndex th Pascal's Triangle
        Args:
            rowIndex(int): row index of Pascal's Triangle (1 <= rowIndex <= 33)
        Returns:
            List[List[int]]: rowIndex th Pascal's Triangle
        '''
        # DP solution
        if rowIndex == 0:
            return [1]

        pascal_triangle = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            cur_row = [1]
            for j in range(1, len(pascal_triangle[i - 1])):
                cur_row.append(pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j - 1])
            cur_row.append(1)
            pascal_triangle.append(cur_row)

        return pascal_triangle[-1]

        # more simple solution
        if rowIndex == 0:
            return [1]

        pascal_triangle = [1] * (rowIndex + 1)

        for row in range(2, rowIndex + 1):
            for idx in reversed(range(1, row)):
                pascal_triangle[idx] += pascal_triangle[idx - 1]

        return pascal_triangle
