Q[118]. Pascal`s Triangle

n: numRows
time: O(n^2)
space: O(n)

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''Compute Pascal's Triangle
        Args:
            numRows(int): raw of Pascal's Triangle (1 <= numRows <= 30)
        Returns:
            List[List[int]]: Pascal's Triangle
        '''
        if numRows == 0:
            raise ValueError('numRows should be [1, 30]')

        if numRows == 1:
            return [[1]]

        pascal_trianlge = [[1], [1, 1]]
        for i in range(2, numRows):
            cur_row = [1]
            for j in range(1, len(pascal_triangle[i - 1])):
                cur_row.append(pascal_triangle[i - 1][j] + pascal_triangle[i - 1][j - 1])
            cur_row.append(1)
            pascal_triangle.append(cur_row)

        return pascal_triangle
