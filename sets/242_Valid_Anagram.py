# n = len(s) or len(t)
# time = O(n)
# space = O(1)
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Args:
            s: str: given strings, 1 <= s.length <= 5*10**4
            t: str: given strings, 1 <= t.length <= 5*10**4
        Returns:
            bool: s and t is anagram
        """
        length_low = 1
        length_high = 5 * 10 ** 4
        if len(s) < length_low or length_high < len(s) or len(t) < length_low or length_high < len(t):
            raise ValueError("length s and t should be one or more and fifty thousand or less")
        s_dic = collections.Counter(s)
        t_dic = collections.Counter(t)
        return s_dic == t_dic