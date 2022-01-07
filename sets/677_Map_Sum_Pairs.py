"""
Trie
n = len(prefix)
m = len(key)

insert function
time = O(m)
space = O(m)

sum function
time = O(n)
space = O(n)
"""
class Trie:
    def __init__(self):
        self.child = defaultdict(Trie)
        self.val = 0
        
class MapSum:

    def __init__(self):
        self.root = Trie()
        self.memory = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.memory.get(key,0)
        self.memory[key] = val
        node = self.root
        for char in key:
            node = node.child[char]
            node.val += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            node = node.child.get(char)
            if not node:
                return 0
            
        return node.val