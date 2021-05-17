# n = minimum length of string in strs
# time = O(n)
# space = O(1)
# done time = 30m


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""

        str_min = min(strs)
        str_max = max(strs)
        common_prefix_length = 0
        for i in range(min(len(str_min), len(str_max))):
            if str_min[i] != str_max[i]:
                break
            common_prefix_length += 1

        return str_min[:common_prefix_length]
