class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ret = 0
        left, right = -1, len(mat[0])
        for i in range(len(mat)):
            ret += mat[i][left+1] + mat[i][right-1] if left + 1 != right - 1 else mat[i][left+1]
            left += 1
            right -= 1
        return ret
