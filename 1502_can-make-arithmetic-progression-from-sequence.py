class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[0] - arr[1]
        for ai, aj in zip(arr, arr[1:]):
            if diff != ai - aj:
                return False
        return True
