Q[119]. Pascals Triangle II


n = rowIndex ([1, 33])
time : O(n^2)
space : O(n)


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

        res = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            cur_res = [1]
            for j in range(1, len(res[i - 1])):
                cur_res.append(res[i - 1][j] + res[i - 1][j - 1])
            cur_res.append(1)
            res.append(cur_res)

        return res[-1]

        # more simple solution
        if rowIndex == 0:
            return [1]

        res = [1] * (rowIndex + 1)

        for row in range(2, rowIndex + 1):
            for idx in reversed(range(1, row)):
                res[idx] += res[idx - 1]

        return res
