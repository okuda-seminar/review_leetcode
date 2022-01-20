'''
Q[77]. Combinations
'''

# time : O(n!) (= nPk)
# space : O(n!) (= nCk)


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        '''Return all posible combinations of k
        Args:
            n(int): the range of number
            k(int): the number of combinations
        Returns:
            List[List[int]]: all posible combinations of k
        '''
        self.n = n
        self.k = k
        self.combinations = []
        path = []
        idx = 1

        self.backtracking(path, idx)

        return self.combinations

    def backtracking(self, path: List[int], idx: int) -> None:
        '''backtrack
        Args:
            path(List[int]): path of nums
            idx(int): index of nums
        '''
        if len(path) == self.k:
            self.combinations.append(path)
            return None

        for i in range(idx, self.n + 1):
            self.backtracking(path + [i], i + 1)
