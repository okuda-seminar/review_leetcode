"""
stack
n = length of self.stack1
# push,peek,empty
time = O(1)
space = O(1)
# pop
time = O(n)
space = O(n)
"""
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        a = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return a

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        return self.stack1 == []