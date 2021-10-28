#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
"""
n = len(input)
time complexity : O(n)
space complexity : O(n)
"""
from collections import deque


# @lc code=start
class MyStack:

    def __init__(self):
        """initialize data structure
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """push element x to the top of the stack

        Args:
            x(int): integer
        """
        print(self.stack)
        self.stack.append(x)

    def pop(self) -> int:
        """Remove the element on the top of the stack and returns it

        Returns:
            int: the element on the top of the stack
        """
        print(self.stack)
        return self.stack.pop()

    def top(self) -> int:
        """return the element on the top of the stack

        Returns:
            int: the element on the top of the stack
        """
        print(self.stack)
        ans = self.stack.pop()
        self.stack.append(ans)
        return ans

    def empty(self) -> bool:
        """return true if the stack is empty, false otherwise

        Returns:
            bool: true if the stack is empty, false otherwise
        """
        print(self.stack)
        return len(self.stack) == 0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
