# n = tiles.length
# time = O(n)
# space = O(n)
# done time = 30m


class Solution:

    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        def dfs(path: str, tile: str) -> None:
            if path:
                res.add(path)
            for i in range(len(tile)):
                dfs(path + tile[i], tile[:i] + tile[i+1:])


        dfs("", tiles)
        return len(res)
