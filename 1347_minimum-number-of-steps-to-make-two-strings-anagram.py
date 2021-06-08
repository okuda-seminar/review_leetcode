# n = s.length
# time = O(n)
# space = O(n)
# done time = 10m


class Solution:

    def minSteps(self, s: str, t: str) -> int:
        s_count_dict, t_count_dict = map(collections.Counter, (s, t))
        return sum((s_count_dict - t_count_dict).values())
