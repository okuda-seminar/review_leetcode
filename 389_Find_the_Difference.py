# n = len(t)
# time = O(n)
# space = O(n)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        Args:
            s (str): strings
            t (str): strings s of adding one letter
        Returns:
            str: the letter that was added to t
        Examples:
            findTheDifference("abcd","abcde") <- "e"
        """
        d = {}
        for i in t:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in s:
            if i in d:
                d[i] -= 1
        for k, v in d.items():
            if v == 1:
                return k