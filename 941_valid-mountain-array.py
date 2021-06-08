# n = arr.lenfth
# time = O(n)
# space = O(1)
# done time = 35m


class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        max_idx = arr.index(max(arr))
        return 0 < max_idx < N - 1 and\
            all(arr[i] < arr[i + 1] for i in range(max_idx))\
            and all(arr[i + 1] < arr[i] for i in range(max_idx, N - 1))
