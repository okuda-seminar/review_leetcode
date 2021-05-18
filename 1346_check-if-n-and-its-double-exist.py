# n = arr.length
# time = O(n)
# space = O(1)
# done time = 20m


class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:
        if 2 <= arr.count(0):
            return True

        arr_set = set(arr)
        div = 2
        for num in arr_set:
            num_half, mod = divmod(num, div)
            if mod != 0:
                continue
            if num_half in arr_set and num_half != 0:
                return True

        return False
