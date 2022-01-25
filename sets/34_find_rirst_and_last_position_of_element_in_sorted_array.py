"""
n : the length of nums
time complexity = O(log n)
space complexity = O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        l, r = self.binary_search(target), self.binary_search(target + 1) - 1
        if l <= r:
            return [l, r]
        
        return [-1, -1]
    
    def binary_search(self, target):
        l, r = 0, len(self.nums)
        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = self.left_bs(nums, target), self.right_bs(nums, target)
        if l <= r:
            return [l, r]
        
        return [-1, -1]
    
    def left_bs(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
    def right_bs(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return r