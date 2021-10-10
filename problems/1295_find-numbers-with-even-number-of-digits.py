class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        digits = [len(str(i)) for i in nums]
        count = 0
        for i in digits:
            if i % 2 == 0:
                count += 1
        return count
