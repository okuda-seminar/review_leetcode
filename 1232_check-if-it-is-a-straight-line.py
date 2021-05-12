# n = coordinates.length
# time = O(n)
# space = O(1)
# done time = 30m


class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        return all(
            (coordinates[i + 1][1] - coordinates[i][1])
            * (coordinates[i + 2][0] - coordinates[i + 1][0])
            == (coordinates[i + 1][0] - coordinates[i][0])
            * (coordinates[i + 2][1] - coordinates[i + 1][1])
            for i in range(len(coordinates) - 2)
        )
