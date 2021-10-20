#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """search a 2D matrix

        Args:
            matrix(List[List[int]]): 2D matrix
            target(int): integer

        Returns:
            bool: return true if target is in matrix, and return false if not in matrix
        """
        if len(matrix) == 0:
            return False

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid // len(matrix[0])][mid % len(matrix[0])] == target:
                return True

            elif matrix[mid // len(matrix[0])][mid % len(matrix[0])] < target:
                left = mid + 1
            
            else: 
                right = mid - 1
        
        return False
# @lc code=end
