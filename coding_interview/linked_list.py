from typing import List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, animal_list: List[str]) -> None:
        self.front = {}
        self.rear = {}
        for animal in animal_list:
            self.front[animal] = self.rear[animal] = None

    def isEmpty(self, animal: str) -> bool:
        return self.front[animal] == None

    def EnQueue(self, item: int, animal: str) -> int:
        temp = ListNode(item)
        if self.rear[animal] == None:
            self.front[animal] = self.rear[animal] = temp
        self.rear[animal].next = temp
        self.rear[animal] = temp
    
    def DeQueue(self, animal: str) -> int:
        if animal == "any":
            ans = float("inf")
            for kind in self.front:
                if self.front[kind] and ans > self.front[kind].val:
                    animal = kind
                    ans = self.front[kind].val

        if self.isEmpty(animal):
            return None
        
        temp = self.front[animal]
        self.front[animal] = temp.next
        if self.front[animal] == None:
            self.rear[animal] = None
        return temp.val

if __name__ == '__main__':
    ans = Solution(["dog", "cat"])
    ans.EnQueue(1, "dog")
    ans.EnQueue(2, "dog")
    ans.EnQueue(3, "dog")
    assert ans.DeQueue("any") == 1, "bad case"