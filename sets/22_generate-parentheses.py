'''
Q[22]. Generate Parentheses
'''

# time : O(2 ** n)
# space : O(2 ** n)

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''Return all combinations of parentheses
        Args:
            n(int): Total number of parentheses (1 <= n <= 8)
        Returns:
            List[str]: all combinations of parentheses
        '''
        if not n:
            raise ValueError('n should be [1, 8]')

        self.subsets = []
        path = '('
        n_left = n - 1
        n_right = n
        self.backtracking(path, n_left, n_right)
        return self.subsets

    def backtracking(self, path: List[int], n_left: int, n_right: int) -> None:
        '''
        Args:
            path(List[int]): current path of nums
            n_left(int): The remaining number of left parentheses
            n_right(int): The remaining number of right parentheses
        '''
        if not n_right:
            self.subsets.append(path)
            return None

        if not n_left:
            n_right -= 1
            self.backtracking(path + ')', n_left, n_right)
        else:
            if n_right - n_left >= 1:
                parentheses = ['(', ')']
                for parenthese in parentheses:
                    if parenthese == '(':
                        n_left -= 1
                        self.backtracking(path + parenthese, n_left, n_right)
                        n_left += 1
                    else:
                        n_right -= 1
                        self.backtracking(path + parenthese, n_left, n_right)
                        n_right += 1
            else:
                n_left -= 1
                self.backtracking(path + '(', n_left, n_right)
                n_left += 1


import copy

from collections import deque


class Solution:
    def generateParenthesis1(self, n: int) -> List[str]:
        """Function to generate all combinations of well-formed parentheses
        Args:
            n(int): integer
        Returns:
            List[str]: all combinations of well-formed parentheses
        """
        ans = []
        queue = deque()
        queue.append([0, 0, []])
        while queue:
            left, right, s = queue.popleft()
            if len(s) == 2 * n:
                ans.append("".join(s))
            if left > right:
                copy_s = copy.deepcopy(s)
                if left < n:
                    s.append("(")
                    queue.append([left + 1, right, s])
                if right < n:
                    copy_s.append(")")
                    queue.append([left, right + 1, copy_s])
            elif left == right:
                copy_s = copy.deepcopy(s)
                if left < n:
                    s.append("(")
                    queue.append([left + 1, right, s])

        return ans