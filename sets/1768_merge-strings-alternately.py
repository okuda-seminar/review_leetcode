Q[1768]. Merge Strings Alternately

n = max(len(word1), len(word2))
time : O(n)
space : O(n)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''Merge strings
        Args:
            word1: consist of lowercase (1 <= len(word1) <= 100)
            word2: consist of lowercase (1 <= len(word2) <= 100)
        Returns:
            str: Merge strings by adding letters in alternating order
        '''
        if not word1 or not word2:
            return ''

        merge_words = []
        word_list1 = list(word1)
        word_list2 = list(word2)
        for str1, str2 in zip(word_list1, word_list2):
            merge_words.append(str1 + str2)

        if len(word1) > len(word2):
            merge_words.append(word1[len(word2):])
        else:
            merge_words.append(word2[len(word1):])

        return ''.join(merge_words)
