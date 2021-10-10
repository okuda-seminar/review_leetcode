class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        ret = []
        for i in range(len(indices)):
            ret.append(s[indices.index(i)])
        return "".join(ret)
