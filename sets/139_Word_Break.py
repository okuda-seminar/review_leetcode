"""
Trie
n = len(WordDict)
m = len(s)
time = O(mn)
space = O(nm)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}

        for word in wordDict:
            node = trie
            for ch in word: 
                node = node.setdefault(ch, {})
            node['#'] = True

        leads = [trie]
        for ch in s:
            new_leads = []
            trie_added = False
            while leads:
                lead = leads.pop()
                if ch not in lead: 
                    continue
                
                lead = lead[ch]
                new_leads.append(lead)
                if '#' in lead and not trie_added:
                    new_leads.append(trie)
                    trie_added = True
            leads = new_leads

        return trie in leads

"""
dynamic programing
n = len(s)
time = O(n^2)
space = O(n)
"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """word break
        Args:
            s (str)
            wordDict (List[str]): dictionary of strings
        Returns:
            bool: if s can be segmented into a space-separated sequence of one or more dictionary words
        Examples:
            wordBreak("leetcode", ["leet", "code"])
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        len_word = [len(x) for x in wordDict]
        max_len, min_len = max(len_word), min(len_word)
        wordDict = set(wordDict)
        for i in range(1,len(s)+1):
            for j in range(i-1, -1, -1):
                if i - j < min_len:
                    continue
                if max_len < i - j:
                    break
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]