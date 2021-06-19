# n = minimum length of string in strs
# time = O(n)
# space = O(1)
# done time = 30m


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for str_triplet in zip(*strs):
            if len(set(str_triplet)) == 1:
                prefix += str_triplet[0]
            else:
                break

        return prefix
