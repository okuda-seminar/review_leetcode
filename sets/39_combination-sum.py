'''
Q[39]. Combination Sum
'''

# n = len(candidates)
# time : 2 ** n
# space : 2 ** n


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''Return all unique combinations of candidates
        Args:
            candidates(List[int]): array consist of distinct integers (1 <= len(candidates) = 30)
            target(int): integer (1 <= target <= 500)
        Returns:
            List[List[int]]: all unique combinations of candidates
        '''
        if not candidates:
            raise ValueError('candidates length should be [1, 30]')

        if not target:
            raise ValueError('candidates length should be [1, 500]')

        self.ans = []
        path = []
        self.backtracking(path, candidates, target)
        return self.ans

    def backtracking(self, path: List[int], candidates: List[int], target: int) -> None:
        '''backtrack candidates
        Args:
            path(List[int]): path of candidates
            candidates(List[int]): array consist of distinct integers
            target(int): integer
        '''

        if target == 0:
            self.ans.append(path)
            return None

        if target < 0:
            return None

        for i in range(len(candidates)):
            self.backtracking(path + [candidates[i]], candidates[i:], target - candidates[i])
