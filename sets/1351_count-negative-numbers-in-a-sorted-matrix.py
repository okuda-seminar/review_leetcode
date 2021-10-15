#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
#

# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """count negatives

        Args:
            grid(List[List[int]]): m * n matrix grid which is stored in nonincreasing order both row-wise and column-wise
        
        Returns:
            int: the number of negative number
        """

        # use binary search
        """
        time complexity : O(mlogn)
        space complexity : O(1)
        """
        """
        ans = 0
        for i in range(len(grid)):
            left = -1
            right = len(grid[0])
            while 1 < right - left:
                mid = (right + left) // 2
                if grid[i][mid] < 0:
                    right = mid
                else:
                    left = mid
            ans += (len(grid[0]) - right)
        return ans
        """

        # use two pointer
        """
        time complexity : O(m + n)
        space complexity : O(1)
        """
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        i = len(grid) - 1
        j = 0
        ans = 0
        while 0 <= i and j < len(grid[0]):
            if grid[i][j] < 0:
                ans += len(grid[0]) - j
                i -= 1
            else: 
                j += 1
        return ans
# @lc code=end

