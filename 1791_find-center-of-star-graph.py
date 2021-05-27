# time = O(1)
# space = O(1)
# done time = 10m


class Solution:

    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]

        return edges[0][1]
