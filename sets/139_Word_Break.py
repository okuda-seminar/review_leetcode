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