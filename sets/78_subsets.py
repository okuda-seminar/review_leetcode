'''
Q[78]. Subsets
'''

# n = len(nums)
# time : O(2 ** n)
# space : O(2 ** n)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''Return possible subsets of nums
        Args:
            nums(List[int]): array of unique elements (1 <= len(nums) <= 10)
        Returns:
            List[List[int]]: all possible subsets of nums
        '''
        if not nums:
            raise ValueError('nums length should be [1, 10]')

        self.subsets = []
        path = []
        self.backtracking(path, nums)
        return self.subsets

    def backtracking(self, path: List[int], nums: List[int]) -> None:
        '''backtrack nums
        Args:
            path(List[int]): current path of nums
            nums(List[int]): array of unique elements
        '''
        self.subsets.append(path)
        if not nums:
            return None

        for i in range(len(nums)):
            self.backtracking(path + [nums[i]], nums[i+1:])


# time : O(n * 2 ** n)
# space : O(2 ** n)


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for n in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [n])
        return subsets
