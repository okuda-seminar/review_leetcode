# n = len(s) = len(t)
# time = O(n)
# space = O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """compute isomorphic
        Args:
            s (str): ascii character (1 <= s.length <= 5*10^4)
            t (str): ascii character (1 <= t.length <= 5*10^4)
        Returns:
            bool: s and t are isomorphic if the characters in s can be replaced to get t
        """
        assert type(s)==str, "type of s should be strings"
        assert type(t)==str, "type of t should be strings"
        length_high = 5 * 10 ** 4
        length_low = 1
        if len(s) < length_low or length_high < len(s) or len(t) < length_low or length_high < len(t):
            raise ValueError("s and t length should be one or more and 5*10^4 or less")
        return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))