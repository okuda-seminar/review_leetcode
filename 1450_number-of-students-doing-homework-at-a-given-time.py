class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([st <= queryTime <= et for st, et in zip(startTime, endTime)])
