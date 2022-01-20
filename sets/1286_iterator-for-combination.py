'''
Q[1286]. Iterator for Combination
'''

# n = len(characters)
# m = combinationLength
# time : O(2**n)
# space : O(nCm)


from collections import deque


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        '''Initialize
        Args:
            characters(str): sorted distinct lowercase letters
            combinationLength(int): the length of combination (1 <= len(combinationLength) <= 15)
        '''
        if not characters:
            raise ValueError('characters should not be empty')

        self.characters = characters
        self.combinationLength = combinationLength
        self.combinations = deque()
        self.backtracking('', 0)

    def backtracking(self, path: str, idx: int) -> None:
        '''Backtracking
        Args:
            path(str): path of combination
            idx(int): index
        '''
        if len(path) == self.combinationLength:
            self.combinations.append(path)
            return None

        for i in range(idx, len(self.characters)):
            self.backtracking(path + self.characters[i], i + 1)

    def next(self) -> str:
        '''Return the next combination
        Returns:
            str: the next combination
        '''
        return self.stack.popleft()

    def hasNext(self) -> bool:
        '''Return True if there exists a next combination
        Returns:
            bool: True if there exists a next combination
        '''
        return True if self.combinations else False
