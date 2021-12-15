from collections import deque
class AnimalQueue:
    def __init__(self, kinds):
        self.queue = {}
        for kind in kinds:
            self.queue[kind] = deque([])
    
    def enqueue(self, kind, index):
        if kind in self.queue:
            self.queue[kind].append(index)
        else:
            self.queue[kind] = deque([index])

    def dequeue(self, kind):
        if kind == "any":
            ans, min_index = self.queue.items()[0]
            for animal, value in self.queue.items():
                if min_index > value:
                    min_index = value
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