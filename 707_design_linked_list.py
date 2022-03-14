class TreeNode:

    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.root = None
        self.length = 0

    def get(self, index: int) -> int:
        if self.length <= index or index < 0:
            return -1
        
        else:
            curr = self.root
            while index > 0:
                curr = curr.next
                index -= 1
            return curr.val

    def addAtHead(self, val: int) -> None:
        node = TreeNode(val)
        node.next = self.root
        self.root = node
        self.length += 1

    def addAtTail(self, val: int) -> None:
        node = TreeNode(val)
        if self.root is None:
            self.root = node
        else:
            curr = self.root
            while curr.next:
                curr = curr.next
            curr.next = node
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if self.length < index:
            return None
        
        elif index <= 0:
            self.addAtHead(val)
        elif self.length == index:
            self.addAtTail(val)
        else:
            node = TreeNode(val)
            i = 0
            curr = self.root
            prev = None
            while i < index:
                prev = curr
                curr = curr.next
                i += 1
            prev.next = node
            node.next = curr
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return None

        elif index == 0:
            self.deleteAtHead()
        elif index == self.length:
            self.deleteAtTail()
        else:
            curr = self.root
            i = 0
            prev = None
            while i < index and curr.next:
                prev = curr
                curr = curr.next
                i += 1
            prev.next = curr.next
            curr = None
            self.length -= 1
     
    def deleteAtHead(self):
        if self.length == 1:
            self.root = None
        else:
            curr = self.root
            self.root = curr.next
            curr = None
        self.length -= 1

    def deleteAtTail(self):
        if self.length == 1:
            self.root = None
        else:
            curr = self.root
            prev = None
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None
            curr = None
        self.length -= 1