'''
Q[1079]. Letter Tile Possibilities
'''

# n = len(tiles)
# time : O(n!)
# space : O(n)


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        '''compute the number of possible non-empty sequences of tiles
        Args:
            tiles(str): string consist of uppercase (1 <= len(tiles) <= 7)
        Returns:
            int: the number of possible non-empty sequences of tiles
        '''
        if not tiles:
            raise ValueError('tiles length should be [1, 7]')

        self.sequence_tiles = set()
        self.backtracking("", tiles)

        return len(self.sequence_tiles)

    def backtracking(self, path: str, tiles: str) -> None:
        '''add possible non-empty sequences of tiles to sequence_tiles
        Args:
            path(str): the path of characters
            tiles(str): tiles
        '''
        if path:
            self.sequence_tiles.add(path)

        if not tiles:
            return None

        for i in range(len(tiles)):
            self.backtracking(path + tiles[i], tiles[:i] + tiles[i+1:])
