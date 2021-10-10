# n = max(s.length, t.length)
# time = O(n)
# space = O(n)
# done time = 30m


class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        def convert(s):
            ret = []
            for c in s:
                if c == '#':
                    if ret:
                        ret.pop()
                else:
                    ret.append(c)
            return ret
        return convert(S) == convert(T)
