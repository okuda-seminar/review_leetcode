#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        time: O(n)
        space: O(n)
        """
        step = [i if i <= 2 else 0 for i in range(n + 2)]
        if 3 <= n:
            for num_step in range(3, n + 1):
                step[num_step] = step[num_step - 1] + step[num_step - 2]
        return step[n]
# @lc code=end

