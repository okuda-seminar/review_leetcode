# n = nums.length
# time = O(n)
# space = O(1)
class NumArray:
    def __init__(self, nums: List[int]):
        self.cumlative_sum = list(accumulate([0] + nums))
        
    def sumRange(self, left: int, right: int) -> int:
        return self.cumlative_sum[right + 1] - self.cumlative_sum[left]
