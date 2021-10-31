#
# @lc app=leetcode id=933 lang=python3
#
# [933] Number of Recent Calls
#

# @lc code=start
from collections import deque


class RecentCounter:

    def __init__(self):
        """Initialize data structure
        """
        self.sliding_window = deque()

    def ping(self, t: int) -> int:
        """Return the number of requests that has happened in the past 3000 milliseconds
        
        Args:
            t(int): integer
        
        Returns:
            int: the number of requests that has happened in the past 3000 milliseconds
        """
        self.sliding_window.append(t)

        while self.sliding_window[0] < t - 3000:
            self.sliding_window.popleft()
        
        return len(self.sliding_window)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# @lc code=end

