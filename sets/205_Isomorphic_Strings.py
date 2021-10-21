# n = len(s) = len(t)
# time = O(n)
# space = O(1)
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
        if len(s) < 1 or 5 * 10**4 < len(s) or len(t) < 1 or 5 * 10**4 < len(t):
            raise ValueError("s and t length should be one or more and 5*10^4 or less")
        return len(set(zip(s, t))) == len(set(s)) and len(set(zip(t, s))) == len(set(t))