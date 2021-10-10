# n = haystack.length
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)

        return -1
