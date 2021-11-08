"""
n = len(sentence)
m = len(word)
time = O(mn)
space = O(1)
"""
class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['*'] = True
        
    def search(self, word: str) -> str:
        node = self.root
        res = ''
        for char in word:
            if char in node:
                res += char
                node = node[char]
                if '*' in node:
                    break
            else:
                break
        return res if '*' in node else word
        
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """Replace words
        Args:
            dictionary (List[str]): many root character
            sentence (str): original sentence
        Returns:
            str: replaced sentence following dictionary
        """
        node = Trie()
        for char in dictionary:
            node.insert(char)
        return ' '.join(map(node.search, sentence.split()))