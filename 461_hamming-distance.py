class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # simplest solution
        # N = max(len(bit(x)), len(bit(y))) <= 31
        # time: O(1)
        # space: O(1)
        return bin(x^y).count("1")
