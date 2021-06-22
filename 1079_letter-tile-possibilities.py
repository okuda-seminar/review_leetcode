# n = tiles.length
# time = O(n)
# space = O(n)
# done time = 30m


class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        self.res = set()

        def dfs(path: str, tile: str) -> None:
            if path:
                self.res.add(path)
            for i in range(len(tile)):
                dfs(path + tile[i], tile[:i] + tile[i+1:])


        dfs("", tiles)
        return len(self.res)
