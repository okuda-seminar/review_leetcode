"""
Trie
n = len(dictionary)
m = len(searchWord)
time = O(nm^2)
space = O(n)
"""
class Trie:
    def __init__(self):
        self.child = defaultdict(Trie)
        self.isEnd = False
        
class MagicDictionary:

    def __init__(self):
        self.root = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            node = self.root
            for char in word:
                node = node.child[char]
            node.isEnd = True
        
    def match(self, node: 'Trie', word: str) -> bool:
        for char in word:
            if char not in node.child:
                return False
            
            node = node.child[char]
        return node.isEnd
        
    def search(self, searchWord: str) -> bool:
        node = self.root
        for i, word in enumerate(searchWord):
            for char in node.child:
                if word != char:
                    if self.match(node.child[char], searchWord[i+1:]):
                        return True

            if word not in node.child:
                return False
            
            node = node.child[word]