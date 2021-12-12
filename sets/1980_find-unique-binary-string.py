'''
Q[1980]. Find Unique Binary String
'''

# n = len(nums)
# time : O(2**n)
# space : O(1)


from typing import List


class Solution:

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        '''Find a binary string of length n that does not appear in nums
        Args:
            nums(List[str]): binary strings(1 <= len(nums) <= 16)
        Returns:
            str: a binary string of length n that does not appear in nums
        '''
        if not nums:
            raise ValueError('nums should not be empty')

        path = ''
        self.nums = nums

        self.backtracking(path)

        return self.not_appear_str

    def backtracking(self, path: str) -> None:
        '''backtrack
        Args:
            path(str): path of binary strings
        '''
        if len(path) == len(self.nums[0]):
            if path not in self.nums:
                self.not_appear_str = path
            return None

        for binary in ['0', '1']:
            self.backtracking(path + binary)
