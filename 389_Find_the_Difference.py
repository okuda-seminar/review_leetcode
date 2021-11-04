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
        count_dict = {}
        for i in t:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        for i in s:
            if i in count_dict:
                count_dict[i] -= 1
        for key, value in count_dict.items():
            if value == 1:
                return key