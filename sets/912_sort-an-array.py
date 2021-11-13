'''
Q[912]. Sort an Array
'''


# n = len(nums)
# time : O(nlogn)
# space : O(n)


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        '''sort nums
        Args:
            nums(List[int]): array consist of integers
        Returns:
            List[int]: sorted nums
        '''
        if len(nums) == 1:
            return nums

        middle = len(nums) // 2
        left = self.sortArray(nums[:middle])
        right = self.sortArray(nums[middle:])

        return self.conquer(left, right)

    def conquer(self, left: List[int], right: List[int]) -> List[int]:
        '''conquer left and right
        Args:
            left(List[int]): Left part of nums
            right(List[int]): right part of nums
        Returns:
            List[int] : conquered array
        '''
        conquer_arr = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] <= right[right_idx]:
                conquer_arr.append(left[left_idx])
                left_idx += 1
            else:
                conquer_arr.append(right[right_idx])
                right_idx += 1

        if left_idx < len(left):
            conquer_arr.extend(left[left_idx:])

        if right_idx < len(right):
            conquer_arr.extend(right[right_idx:])

        return conquer_arr


# time : O(nlogn)
# space : O(1)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            raise ValueError('nums length should be [1, 5 * 10**4]')

        return sorted(nums)
