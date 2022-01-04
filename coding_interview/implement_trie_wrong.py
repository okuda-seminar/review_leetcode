"""
Designing Search functions that allow for one-character differences
"""
from collections import deque
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
        curr = self.root
        idx = 0
        cnt = 0
        queue = deque()
        queue.append((curr, idx, cnt))
        while queue:
            curr, idx, cnt = queue.popleft()
            if idx == len(word):
                break
            if word[idx] not in curr:
                if cnt == 0:
                    for node in curr.values():
                        queue.append((node, idx + 1, cnt + 1))
                else:
                    if not queue:
                        return False
 
            else:
                curr = curr[word[idx]]
                queue.append((curr, idx + 1, cnt))
        return curr[self.eos]

if __name__ == '__main__':
    trie = Trie()
    trie.insert("word")
    trie.insert("work")
    trie.insert("wolk")
    trie.insert("will")
    assert trie.search("wars") == False, "bad case"