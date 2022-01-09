#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
class FrontMiddleBackQueue:

    def __init__(self):
        """Initialize data structure
        """
        self.queue = []

    def pushFront(self, val: int) -> None:
        """Add val to the front of the queue
        
        Args:
            val(int): integer
        """
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        """Add val to the middle of the queue
        
        Args:
            val(int): integer
        """
        self.queue.insert(len(self.queue) // 2, val)

    def pushBack(self, val: int) -> None:
        """Add val to the back of the queue
        
        Args:
            val(int): integer
        """
        self.queue.append(val)

    def popFront(self) -> int:
        """Remove the front element of the queue and return it
        
        Returns:
            int: integer
        """
        if len(self.queue) == 0:
            return -1
        return self.queue.pop(0)

    def popMiddle(self) -> int:
        """Remove the middle element of the queue and return it
        
        Returns:
            int: integer
        """
        if len(self.queue) == 0:
            return -1
        return self.queue.pop((len(self.queue) - 1) // 2)

    def popBack(self) -> int:
        """Remove the back element of the queue and return it
        
        Returns:
            int: integer
        """
        if len(self.queue) == 0:
            return -1
        return self.queue.pop()
# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end

