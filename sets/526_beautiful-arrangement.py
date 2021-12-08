'''
Q[526]. Beautiful Arrangement
'''

# time : O(n!)
# space : O(n)


class Solution:
    def countArrangement(self, n: int) -> int:
        '''Returns the number of the beautiful arrangements
        Args:
            n(int): integer (1 <= n <= 15)
        Returns:
            int: the number of the beautiful arrangements
        '''
        if n == 0:
            raise ValueError('n should be [1, 15]')

        self.n = n
        self.beautiful_arrangement_num = 0
        cur_idx = 1
        perm = {i for i in range(1, n + 1)}

        self.backtracking(cur_idx, perm)

        return self.beautiful_arrangement_num


    def backtracking(self, cur_idx: int, perm: set) -> None:
        '''backtrack
        Args:
            cur_idx(int): current index
            perm(set): kinds of numbers
        '''
        if cur_idx == self.n + 1:
            self.beautiful_arrangement_num += 1
            return None

        for num in perm:
            if cur_idx % num == 0 or num % cur_idx == 0:
                self.backtracking(cur_idx + 1, perm - {num})
