from typing import List
class SequentialGroup:

    def __init__(self):
        self.ans = []

    def sequential_group(self, array: List[int]) -> List[List[int]]:
        array.sort()
        start = 0
        self.ans = []
        for i in range(1,len(array)):
            if array[i-1] + 1 < array[i]:
                if start != i-1:
                    self.ans.append([array[start],array[i-1]])
                else:
                    self.ans.append([array[start]])
                start = i
        if start <= len(array) - 1:
            if start != len(array) - 1:
                self.ans.append([array[start],array[len(array) - 1]])
            else:
                self.ans.append([array[len(array)-1]])
        
        return self.ans

    def search(self, target: int) -> List[int]:
        for list in self.ans:
            if len(list) == 1 and list[0] == target:
                return list
            
            if len(list) == 2 and list[0] <= target <= list[1]:
                return list

seq = SequentialGroup()
assert seq.sequential_group([1,2,3,4,6,7,8])==[[1,4],[6,8]], "bad"
assert seq.sequential_group([1,2,3,4,6,7,8,10])==[[1,4],[6,8],[10]], "bad"
assert seq.sequential_group([1,3,4,6,7,8,10])==[[1],[3,4],[6,8],[10]], "bad"
assert seq.search(5) == None, "bad"
assert seq.search(7) == [6,8], "bad"