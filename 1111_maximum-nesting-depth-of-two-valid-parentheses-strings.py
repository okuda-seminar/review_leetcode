# n = seq.length
# time = O(n)
# space = O(1)
# done time = 10m


class Solution:

    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        depth = 0
        for parenthese in seq:
            if parenthese == '(':
                depth += 1
            res.append(depth % 2) 
            if parenthese == ')':
                depth -= 1

        return res
