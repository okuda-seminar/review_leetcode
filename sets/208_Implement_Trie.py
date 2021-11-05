"""
n = length of word
m = length of prefix

def insert time complexity = O(n)
def search time complexity = O(n)
def prefix time complexity = O(m)
space complexity = O(n)
"""
class Trie:

    def __init__(self):
        self.root = {}
        self.end = '*'

    def insert(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node:
                node[i] = {}
                node = node[i]
            else:
                node = node[i]
        node[self.end] = True
            
    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node:
                return False
            else:
                node = node[i]
        return self.end in node
            
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in prefix:
            if i not in node:
                return False
            else:
                node = node[i]
        return True