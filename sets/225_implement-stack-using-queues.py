#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
from collections import deque


# @lc code=start

# use stack fanction
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
        self.stack.append(x)

    def pop(self) -> int:
        """Remove the element on the top of the stack and returns it

        Returns:
            int: the element on the top of the stack
        """
        return self.stack.pop()

    def top(self) -> int:
        """return the element on the top of the stack

        Returns:
            int: the element on the top of the stack
        """
        return self.stack[-1]

    def empty(self) -> bool:
        """return true if the stack is empty, false otherwise

        Returns:
            bool: true if the stack is empty, false otherwise
        """
        return len(self.stack) == 0


# use queue
class MyStack:

    def __init__(self):
        """initialize data structure
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """push element x to the top of the stack

        Args:
            x(int): integer
        """
        self.queue.append(x)

    def pop(self) -> int:
        """Remove the element on the top of the stack and returns it

        Returns:
            int: the element on the top of the stack
        """
        tmp = self.queue
        self.queue = deque()
        for _ in range(len(tmp) - 1):
            self.queue.append(tmp.popleft())
        return tmp.popleft()

    def top(self) -> int:
        """return the element on the top of the stack

        Returns:
            int: the element on the top of the stack
        """
        return self.queue[-1]

    def empty(self) -> bool:
        """return true if the stack is empty, false otherwise

        Returns:
            bool: true if the stack is empty, false otherwise
        """
        return len(self.queue) == 0
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end
