# sliding window + hash map
# n = length of s
# m = length of p
# time = O(m + n)
# space = O(m + n)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Args:
            s: str: substring
            p: str: string of anagram
        Returns:
            List[int]: s' index of anagram
        Example:
            s = "abcba", p = "abc" <- [0, 2]
        """
        anagram = []
        # create hush map
        count = [0] * 26
        for c in p:
            count[ord(c)-ord('a')] += 1
        # sliding window
        start, end, sz = 0, 0, len(p)
        so_far = len(p)
        
        for c in s:
            if end - start >= sz:
                tmp = s[start]
                count[ord(tmp) - ord('a')] += 1
                
                if count[ord(tmp) - ord('a')] > 0:
                    so_far += 1
                start += 1
            tmp = s[end]
            count[ord(tmp) - ord('a')] -= 1
            if count[ord(tmp) - ord('a')] >= 0:
                so_far -= 1
            if so_far == 0:
                anagram.append(start)
            end += 1
        return anagram




# time exceed
# n = length of s
# m = length of p
# time = O(n * m)
# space = O(n + m)
class Solution:
    def isAnagram(self, s: str, p: str) -> bool:
        """
        n = length of s or p
        time = O(n)
        """
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in p:
            if i in d:
                d[i] -= 1
            else:
                return False

        for k, v in d.items():
            if v != 0:
                return False
                
        return True
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Args:
            s: str: substring
            p: str: string of anagram
        Returns:
            List[int]: s' index of anagram
        Example:
            s = "abcba", p = "abc" <- [0, 2]
        """
        len_p = len(p)
        print(len_p)
        ans = []
        for i in range(len(s) - len_p + 1):
            if self.isAnagram(s[i:(i+len_p)], p):
                ans.append(i)
        return ans