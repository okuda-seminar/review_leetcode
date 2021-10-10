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
        if not 1 <= len(strs) <= 10**4:
            raise ValueError("length of strs is one or more and ten thousand or less")
        dic = defaultdict(list)
        for s in strs:
            if not 0 <= len(s) <= 100:
                raise ValueError("length of strs[i] is zero or more and a hundred or less")
            dic[''.join(sorted(s))].append(s)
        return dic.values()