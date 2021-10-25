"""
A1. heap
n = len(score)
time = O(n)
space = O(n)
"""
import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """compute athlete ranks
        Args:
            score (List[int]): integer array include athlete score
        Returns:
            List[str]: array of each athlete's rank
        Examples:
            findRelativeRanks([2,4,6,3,1]) <- ["4", "Silber Medal", "Gold Medal", "Bronze Medal", "5"]
        """
        score_index = [[v * -1,i] for i,v in enumerate(score)]
        l = len(score_index)
        heapq.heapify(score_index)
        ans = [0] * l
        for i in range(l):
            hid = heapq.heappop(score_index)[1]
            if i == 0:
                ans[hid] = "Gold Medal"
            elif i == 1:
                ans[hid] = "Silver Medal"
            elif i == 2:
                ans[hid] = "Bronze Medal"
            else:
                ans[hid] = str(i + 1)
        return ans

"""
A.2 sort + hash map
n = len(score)
time = O(n)
space = O(n)
"""
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        """compute athlete ranks
        Args:
            score (List[int]): integer array include athlete score
        Returns:
            List[str]: array of each athlete's rank
        Examples:
            findRelativeRanks([2,4,6,3,1]) <- ["4", "Silber Medal", "Gold Medal", "Bronze Medal", "5"]
        """
        d = {v:i>2 and str(i+1) or ["Gold", "Silver", "Bronze"][i]+" Medal" for i,v in enumerate(sorted(score, reverse=True))}
        return [d[num] for num in score]