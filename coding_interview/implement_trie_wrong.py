"""
Designing Search functions that allow for one-character differences
"""
class Trie:
    
    def __init__(self):
        self.root = {}
        self.eos = "*"
        
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.eos] = True
        
    def search(self, word: str) -> bool:
        node = self.root
        cnt = 0
        for char in word:
            if char in node:
                node = node[char]
            
            else:
                for d in node.values():
                    node = d
                cnt += 1
                if cnt > 1:
                    return False
                
        return self.eos in node
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            
            node = node[char]
        return True

"""
Future Policy
 Problem: Cannot handle cases where multiple characters are contained in a dictionary.
 Solution: using deque
""" 