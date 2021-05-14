# n = s.length
# time = O(n)
# space = O(1)
# done time = 15m


class Solution:

    def countSegments(self, s: str) -> int:
        s_strip = s.strip()
        if not s_strip:
            return 0

        segment_count = 0
        for i in range(len(s_strip)):
            if s_strip[i] == ' ' and s_strip[i - 1] != ' ':
                segment_count += 1

        return segment_count + 1
