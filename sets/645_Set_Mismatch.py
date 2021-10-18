# n = len(nums)
# time = O(n)
# space = O(1)
from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        Args:
            nums (List[int]): array of integers, which got duplicated on one of the duplicated 
        Returns:
            List[int]: repetition of one number and loss of another number
        Examples:
            findErrorNums([1,2,2,4,5]) <- [2,3]
        """
        c = Counter(nums)
        dup = c.most_common()[0][0]
        for i in range(1,len(nums)+1):
            if not i in c:
                break;
        return [dup,i]