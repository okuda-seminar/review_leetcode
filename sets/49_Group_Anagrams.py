# n = strs' length
# m = strs[i]'s length
# time = O(n * mlogm)
# space = O(n * m)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Args:
            strs: List[str]: array of strings
        Returns:
            List[List[str]]: group the anagrams
        Examples:
            strs = ["tea", "bat", "ate"] -> [["bat"],["ate","tea"]]
        """
        length_low = 1
        length_high = 10 ** 4
        string_low = 0
        string_high = 100
        if len(strs) <length_low or length_high < len(strs):
            raise ValueError("length of strs is one or more and ten thousand or less")
        dic = defaultdict(list)
        for s in strs:
            if len(s) < string_low or string_high < len(s):
                raise ValueError("length of strs[i] is zero or more and a hundred or less")
            dic[''.join(sorted(s))].append(s)
        return dic.values()