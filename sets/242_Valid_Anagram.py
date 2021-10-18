# n = len(s) or len(t)
# time = O(n)
# space = O(1)
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Args:
            s: str: given strings, 1 <= s.length <= 5*10**4
            t: str: given strings, 1 <= s.length <= 5*10**4
        Returns:
            bool: s and t is anagram
        """
        assert len(s) != 0, "length of s is one or more"
        assert len(t) != 0, "length of t is one or more"
        s_dic = collections.Counter(s)
        t_dic = collections.Counter(t)
        return s_dic == t_dic