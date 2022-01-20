'''
Q[784]. Letter Case Permutation
'''

# n = len(s)
# time : O(n**3)
# space : O(2**n)

)
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        '''compute all posible strings, taking lowercase and uppercase into account
        Args:
            s(str): string consist of letters or digits (1 <= len(s) <= 12)
        Returns:
            List[str]: all posible strings, taking lowercase and uppercase into account
        '''
        if not s:
            raise ValueError('s length should be [1, 12]')

        self.s = s
        s_list = list(s)
        self.letter_case_permutation = []
        path = ""
        self.backtracking(path, s_list)
        return self.letter_case_permutation

    def backtracking(self, path: str, s: List[str]) -> None:
        '''
        Args:
            path: path of s
            s: given string
        '''
        if len(path) == len(self.s):
            self.letter_case_permutation.append(path)

        if not s:
            return None

        for i in range(len(s)):
            self.backtracking(path + s[i], s[i+1:])
            if s[i].islower():
                s[i] = s[i].upper()
                self.backtracking(path + s[i], s[i+1:])
            elif s[i].isupper():
                s[i] = s[i].lower()
                self.backtracking(path + s[i], s[i+1:])
