class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        return sum([int(sh != h) for sh, h in zip(sorted_heights, heights)])
