'''
12/4 coding interview

Example:
    sum_target(k = 10, target = 5) ->
    [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3],
    [1, 2, 2], [1, 4], [2, 3], [5]]
'''

# n = target
# time : O(n**k)
# space : O(k)


from typing import List


class Solution:
    def sum_target(self, k:int, target:int) -> List[List[int]]:
        nums = [i for i in range(1, k + 1)]
        self.target = target
        self.res = []
        self.backtracking([], nums, target)
        return self.res

    
    def backtracking(self, path:List[int], nums:List[int], target:int) -> None:
        if target == 0:
            self.res.append(path)
            return None

        if target < 0:
            return None

        for i in range(len(nums)):
            self.backtracking(path + [nums[i]], nums[i:], target - nums[i])
