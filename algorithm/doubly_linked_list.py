"""
Implement two way queue using doubly linked list
n : length of the doubly linked list
In pushleft, push, popleft, pop functions
    time complexity = O(1)
    space complexity = O(n)
"""


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def print_doubly_linked_list(self):
        temp = self.head
        while temp:
            print(temp.val, end=' ')
            temp = temp.next
        print("")

    def pushleft(self, val: int) -> None:
        temp = ListNode(val)
        if self.head is None:
            self.head = temp
            self.tail = temp
        else:
            temp.prev = None
            temp.next = self.head
            self.head.prev = temp
            self.head = temp

    def push(self, val: int) -> None:
        temp = ListNode(val)
        if self.tail is None:
            self.head = temp
            self.tail = temp
        else:
            temp.next = None
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp

    def popleft(self) -> int:
        temp = self.head
        if temp is None:
            raise ValueError("DoublyLinkedList should not be empty")
        out = temp.val
        if temp.next is not None:
            temp.next.prev = None
            temp = temp.next
            self.head = temp
        else:
            temp = None
            self.tail = temp
        self.head = temp
        return out

    def pop(self) -> int:
        temp = self.tail
        if temp is None:
            raise ValueError("DoublyLinkedList should not be empty")
        out = temp.val
        if temp.prev is not None:
            temp.prev.next = None
            temp = temp.prev
        else:
            temp = None
            self.head = temp
        self.tail = temp
        return out


if __name__ == '__main__':
    ans = DoublyLinkedList()
    ans.pushleft(3)
    ans.push(1)
    assert ans.pop() == 1, "Error"
    ans.pushleft(1)
    assert ans.pop() == 3, "Error"
    assert ans.pop() == 1, "Error"
    ans.pushleft(3)
    ans.push(1)
    assert ans.popleft() == 3, "Error"
    ans.pushleft(1)
    assert ans.popleft() == 1, "Error"
    assert ans.popleft() == 1, "Error"