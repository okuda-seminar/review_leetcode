"""
A hashmap
n = len(words)
time = O(n)
space = O(n)
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_dict = {}
        for word in words:
            if not word in word_dict:
                word_dict[word] = 1
            else:
                word_dict[word] += 1
        word_list = sorted(word_dict, key=lambda x: (-word_dict[x], x))
        return word_list[:k]