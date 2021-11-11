'''
Q[932]. Beautiful Array

time : O(n)
space : O(n)
'''


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        '''compute beatiful array
        Args
            n(int): integer (1 <= n <= 1000)
        Returns:
            List[int]: beatiful array (not 2*nums[k] == nums[i] + nums[j])
        '''
        if not n:
            raise ValueError('n should be [1, 1000]')

        arr = list(range(1, n + 1))
        return self.divide(arr)

    def divide(self, arr: List[int]) -> List[int]:
        '''divide and conquer the array
        Args:
            arr(List[int]): array (the range is [1, n])
        Returns
            List[int]: beatiful array
        '''
        if len(arr) == 1:
            return arr

        odd = [v for i, v in enumerate(arr) if i % 2 == 1]
        even = [v for i, v, in enumerate(arr) if i % 2 == 0]
        odd = self.divide(odd)
        even = self.divide(even)

        return odd + even
