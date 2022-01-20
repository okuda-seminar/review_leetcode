'''
Q[216]. Combination Sum III
'''

# time : O(n)
# space : O(n)

class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''Return a list of all possible valid combinations
        Args:
            k(int): Number of elements to combine (2 <= n <= 9)
            n(int): sum of combination (1 <= n <= 60)
        Returns:
            List[List[int]]: a list of all possible valid combinations
        '''
        if not k:
            raise ValueError('k should be [2, 9]')

        if not n:
            raise ValueError('n should be [1, 60]')

        self.combination = []
        self.n = n
        self.k = k
        self.backtracking(1, [])
        return self.combination

    def backtracking(self, start: int, path: List[int]) -> None:
        '''Backtrack combinations that are n
        Args:
            start: start index
            path: path of combination
        '''
        if sum(path) > self.n or len(path) > self.k:
            return None

        if sum(path) == self.n:
            if len(path) == self.k:
                self.combination.append(path)
            return None

        VALID_MAX_NUM = 9
        for i in range(start, VALID_MAX_NUM + 1):
            self.backtracking(i + 1, path + [i])
