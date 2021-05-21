class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            for j in range(i, len(arr)-1):
                if abs(arr[i] - arr[j+1]) <= a:
                    for k in range(j+1, len(arr)-1):
                        if abs(arr[j+1] - arr[k+1]) <= b and abs(arr[i] - arr[k+1]) <= c:
                            count += 1
        return count
