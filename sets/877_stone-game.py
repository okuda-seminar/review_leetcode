'''
Q[877]. Stone Game
'''

# n = len(piles)
# time : O(n)
# space : O(n)

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''Determine the victory or defeat of the stone game
        Args:
            piles(List[int]): the number of pile (2 <= len(piles) <= 500)
        Returns:
            bool: True if Alice win
        '''
        if not piles:
            raise ValueError('piles length should be [2, 500]')

        if len(piles) % 2 != 0:
            raise ValueError('piles length should be even')

        Alice_num = [0]
        Bob_num = [0]
        for i in range(len(piles) // 2):
            Alice_num.append(max(
                piles[i] + Bob[-1],
                piles[i] + Alice[-1],
                piles[-i-1] + Bob[-1],
                piles[-i-1] + Alice[-1])
            )
            Bob_num.append(min(
                piles[i] + Bob[-1],
                piles[i] + Alice[-1],
                piles[-i-1] + Bob[-1],
                piles[-i-1] + Alice[-1])
            )

        return Alice_num[-1] > Bob_num[-1]
