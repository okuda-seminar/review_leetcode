"""
n = len(word)
addWord:
    time = O(n)
    space = O(n)

search:
    time = O(n) or O(n^2)
    space = O(1)
"""
class WordDictionary:
    """add and search words
    Attributes:
        word (str): target of word on add or search
    
    """
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        """add word"""
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        
        node['*'] = True

    def search(self, word: str) -> bool:
        """search word"""
        def helper(word, node):
            for i, char in enumerate(word):
                if char in node:
                    node = node[char]
                else:
                    if char == '.':
                        for x in node:
                            if x != '*' and helper(word[i+1:], node[x]):
                                return True
                    return False
            return '*' in node
			
        return helper(word, self.root)