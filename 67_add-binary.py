# n = max(a, b)
# time = O(n)
# space = O(1)
# done time = 10m

class Solution:

    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2: ]
