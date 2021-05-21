# n = arr.lenfth
# time = O(n)
# space = O(1)
# done time = 35m


class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        increase = decrease = False

        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False

            elif arr[i] < arr[i-1]:
                if decrease:
                    return False

                increase = True
            else:
                if not increase:
                    return False

                decrease = True

        return increase and decrease
