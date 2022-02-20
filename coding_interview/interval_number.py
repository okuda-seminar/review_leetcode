from typing import List
class Group:
    def interval_number(self, array:List[int], target: int) -> List[int]:
        end = len(array) - 1
        start = 0
        while start + 1 < end:
            mid = (start + end) // 2
            if array[mid] <= target:
                start = mid
            elif target < array[mid]:
                end = mid
        return [array[start], array[end]]

array1 = [1,2,3,5,7,8]
array2 = [1,3,4,5,9]
ans = Group()
assert ans.interval_number(array2, 2) == [1,3], "bad"
assert ans.interval_number(array1, 4) == [3,5], "bad"