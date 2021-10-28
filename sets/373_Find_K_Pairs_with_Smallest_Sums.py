"""
A1 itertools
n = len(nums1)
m = len(nums2)
time = O(mn logmn)
space = O(mn)
"""
import itertools
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Args:
            nums1 (List[int]): integer arrays sorted in ascending order (1 <= nums1.length <= 10^5, -10^9 <= nums1[i] <= 10^9)
            nums2 (List[int]): integer arrays sorted in ascending order (1 <= nums2.length <= 10^5, -10^9 <= nums2[i] <= 10^9)
            k (int): output number of smallest pairs
        Returns:
            List[List[int]]: the first k pairs list
        """ 
        return sorted(itertools.product(nums1,nums2),key=sum)[:k]
"""
A2. heap + itertools
n = len(nums1)
m = len(nums2)
time = O(mn logk)
space = O(k)
"""
import heapq
import itertools
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Args:
            nums1 (List[int]): integer arrays sorted in ascending order (1 <= nums1.length <= 10^5, -10^9 <= nums1[i] <= 10^9)
            nums2 (List[int]): integer arrays sorted in ascending order (1 <= nums2.length <= 10^5, -10^9 <= nums2[i] <= 10^9)
            k (int): output number of smallest pairs
        Returns:
            List[List[int]]: the first k pairs list
        """ 
        return map(list, heapq.nsmallest(k, itertools.product(nums1, nums2), key=sum))
"""
A3 efficient
n = len(nums1)
m = len(nums2)
time = O(m + k * log m)
space = O(m)
"""
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Args:
            nums1 (List[int]): integer arrays sorted in ascending order (1 <= nums1.length <= 10^5, -10^9 <= nums1[i] <= 10^9)
            nums2 (List[int]): integer arrays sorted in ascending order (1 <= nums2.length <= 10^5, -10^9 <= nums2[i] <= 10^9)
            k (int): output number of smallest pairs
        Returns:
            List[List[int]]: the first k pairs list
        """ 
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]
"""
A4 heap
time = O(k * log k)
space = O(k)
"""
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        Args:
            nums1 (List[int]): integer arrays sorted in ascending order (1 <= nums1.length <= 10^5, -10^9 <= nums1[i] <= 10^9)
            nums2 (List[int]): integer arrays sorted in ascending order (1 <= nums2.length <= 10^5, -10^9 <= nums2[i] <= 10^9)
            k (int): output number of smallest pairs
        Returns:
            List[List[int]]: the first k pairs list
        """ 
        res = []
        m, n, visited = len(nums1), len(nums2), set()
        if m == 0 or n == 0: return [] 
        h = [(nums1[0]+nums2[0], (0, 0))]
        for _ in range(min(k, (m*n))):
            val, (i, j) = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            if i+1 < m and (i+1, j) not in visited:
                heapq.heappush(h, (nums1[i+1]+nums2[j], (i+1, j)))
                visited.add((i+1, j))
            if j+1 < n and (i, j+1) not in visited:
                heapq.heappush(h, (nums1[i]+nums2[j+1], (i, j+1)))
                visited.add((i, j+1))
        return res