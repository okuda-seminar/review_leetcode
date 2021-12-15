from typing import List
from collections import deque
"""
Q1. Implementation of a deque that obtains the index number of 
a specific element over known elements
time = O(1)
space = O(n)
"""
class AnimalQueue:
    def __init__(self, kinds: List[str]) -> None:
        self.queue = {}
        for kind in kinds:
            self.queue[kind] = deque([])
    
    def enqueue(self, kind: str, index: int) -> None:
        if kind in self.queue:
            self.queue[kind].append(index)
        else:
            raise KeyError("{} does not exist".format(kind))

    def dequeue(self, kind: str) -> int:
        if kind in self.queue:
            if not self.queue[kind]:
                raise IndexError("pop from an empty deque")

            return self.queue[kind].popleft()

        else:
            raise KeyError("{} does not exist.".format(kind))
        
# Test Case
# animal_list = ["dog","cat"]
# Queue = AnimalQueue(animal_list)
# Queue.enqueue("cat", 1)
# Queue.enqueue("cat", 2)
# Queue.dequeue("cat") -> 1
# Queue.depueue("dog") -> "pop from an empty deque"
# Queue.enqueue("bird", 3) -> "bird dose not exist"
# Queue.dequeue("bird") -> "bird dose not exist"

"""
Q2. Implementation of a deque that obtains the index number of 
a specific element, including unknown elements
time = O(1)
space = O(n)
"""
from collections import deque
class AnimalQueue:
    def __init__(self, kinds: List[str]) -> None:
        self.queue = {}
        for kind in kinds:
            self.queue[kind] = deque([])
    
    def enqueue(self, kind: str, index: int) -> None:
        if kind in self.queue:
            self.queue[kind].append(index)
        else:
            self.queue[kind] = deque([index])

    def dequeue(self, kind: str) -> int:
        if kind in self.queue:
            if not self.queue[kind]:
                raise IndexError("pop from an empty deque")
            return self.queue[kind].popleft()
        else:
          raise KeyError("{} does not exist.".format(kind))

# Test Case
# animal_list = ["dog", "cat"]
# Queue = AnimalQueue(animal_list)
# Queue.enqueue("cat", 1)
# Queue.enqueue("cat", 2)
# Queue.dequeue("cat") -> 1
# Queue.depueue("dog") -> "pop from an empty deque"
# Queue.enqueue("bird", 3)
# Queue.dequeue("bird") -> 3
# Queue.dequeue("monkey") -> "monkey does not exist."
"""
import unittest
import time
class Test(unittest.TestCase):
    def test_measure_time(self):
        start_time = time.process_time()
        self.test_case()
        end_time = time.process_time()
        elapsed_time = end_time - start_time
        print(elapsed_time)

    def test_case(self):
        animal_list = ["dog", "cat"]
        Queue = AnimalQueue(animal_list)
        Queue.enqueue("cat", 0)
        Queue.enqueue("cat", 1)
        Queue.enqueue("dog", 2)
        Queue.enqueue("bird", 3)
        self.assertEqual(Queue.dequeue("dog"), 2)
        self.assertEqual(Queue.dequeue("cat"), 0)
        self.assertEqual(Queue.dequeue("bird"), 3)

if __name__ == '__main__':
    unittest.main()
"""
"""
Q3. Implementation of a deque that obtains the index number of 
a specific element and if any argument is called retrieves the first element stored.
time = O(1)
space = O(n)
"""
from collections import deque
class AnimalQueue:
    def __init__(self, kinds: List[str]) -> None:
        self.queue = {}
        for kind in kinds:
            self.queue[kind] = deque([])
    
    def enqueue(self, kind: str, index: int) -> None:
        if kind in self.queue:
            self.queue[kind].append(index)
        else:
            self.queue[kind] = deque([index])

    def dequeue(self, kind: str) -> int:
        if kind == "any":
            min_index = float("inf")
            ans = self.queue.keys()[0]
            for animal, value in self.queue.items():
                if min_index > value:
                    ans = animal
            return self.queue[ans].popleft()

        if kind in self.queue:
            if not self.queue[kind]:
                raise IndexError("pop from an empty deque")

            return self.queue[kind].popleft()
        else:
          raise KeyError("{} does not exist.".format(kind))

animal_list = ["dog", "cat"]
Queue = AnimalQueue(animal_list)
Queue.enqueue("cat", 1)
Queue.enqueue("cat", 2)
Queue.enqueue("cat", 3)
Queue.enqueue("dog", 4)
Queue.enqueue("dog", 5)
assert Queue.dequeue("cat") == 1, "False"
assert Queue.dequeue("dog") == 4, "False"
assert Queue.dequeue("any") == 2, "False"