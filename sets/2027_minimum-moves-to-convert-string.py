'''
Q[2027]. Minimum Moves to Convert String

n = len(s)
time : O(n)
space : O(1)
'''

class Solution:
    def minimumMoves(self, s: str) -> int:
        '''compute the minimum number of moves
        Args:
            s(str): string consist of 'X' or 'O' (3 <= len(s) <= 1000)
        Returns:
            int: the minimum number of moves (move is that convert three consecutive characters of s to 'O')
        '''
        if not s:
            raise ValueError('s lenght should be [3, 1000]')
            
        move_idx = 0
        minimum_moves = 0
        while move_idx < len(s):
            if s[move_idx] == 'O':
                move_idx += 1
            else:
                move_idx += 3
                minimum_moves += 1
        
        return minimum_moves
