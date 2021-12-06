#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from collections import deque


"""
time complexity : O(1)
space complexity : O(1)
"""
class MyQueue1:

    def __init__(self):
        """Initialize data structure
        """
        self.stack = []

    def push(self, x: int) -> None:
        """Push element x to the top of the stack

        Args:
            x(int): integer
        """
        self.stack.append(x)

    def pop(self) -> int:
        """Remove the element on the top of the stack and returns it

        Returns:
            int: the element on the top of the stack
        """
        return self.stack.pop(0)

    def peek(self) -> int:
        """Returns the element at the front of the stack

        Returns:
            int: the element on the front of the stack
        """
        return self.stack[0]

    def empty(self) -> bool:
        """Return true if the stack is empty, false otherwise

        Returns:
            bool: true if the stack is empty, false otherwise
        """
        return len(self.stack) == 0


"""
time complexity : O(n)
space complexity : O(1)
"""
class MyQueue:

    def __init__(self):
        """Initialize data structure
        """
        self.stack = deque()

    def push(self, x: int) -> None:
        """Push element x to the top of the stack

        Args:
            x(int): integer
        """
        self.stack.append(x)

    def pop(self) -> int:
        """Remove the element on the top of the stack and returns it

        Returns:
            int: the element on the top of the stack
        """
        tmp = deque()
        for _ in range(len(self.stack) - 1):
            tmp.append(self.stack.pop())
        result = self.stack.pop()

        for _ in range(len(tmp)):
            self.stack.append(tmp.pop())

        return result

    def peek(self) -> int:
        """Returns the element at the front of the stack

        Returns:
            int: the element on the front of the stack
        """
        return self.stack[0]

    def empty(self) -> bool:
        """Return true if the stack is empty, false otherwise

        Returns:
            bool: true if the stack is empty, false otherwise
        """
        return not self.stack
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
