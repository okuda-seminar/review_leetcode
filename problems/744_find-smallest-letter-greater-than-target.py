# n = letters.length
# time = O(n)
# space = O(1)
# done time = 5m


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for s in letters:
            if ord(target) < ord(s):
                return s
        return letters[0]
