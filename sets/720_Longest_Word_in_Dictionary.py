"""
A Trie
n = len(words)
m = len(words[0])
time = O(mnlog n)
space = O(n)
"""
class TreeNode:
    def __init__(self):
        self.child = defaultdict(TreeNode)
        self.word = ""
        self.length = 0

class Trie:
    def __init__(self):
        self.root = TreeNode()
        self.word = ""
        self.max_length = 0
    
    def insert(self, word: str) -> None:
        current = self.root
        word_length = 1
        for letter in word:
            if current.word:
                word_length += 1   
            current = current.child[letter]
        current.word = word
        current.length = word_length if len(word) == word_length else -1
        if current.length > self.max_length:
            self.max_length = current.length
            self.word = current.word
        elif current.length == self.max_length:
            self.word = min(self.word, current.word)
            
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        for word in sorted(words):
            root.insert(word)
        return root.word
"""
A sort + hashmap
n = len(words)
time = O(nlog n)
space = O(n)
"""
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        print(words)
        words_set, words_ans = set(), ""
        words_set.add("")
        for word in words:
            if word[:-1] in words_set:
                words_set.add(word)
                if len(word) > len(words_ans):
                    words_ans = word
                    
        return words_ans