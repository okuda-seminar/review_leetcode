# n = length of nums
# time = O(nlogn)
# space = O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Args:
            nums (List[int]): integer array called nums
            k (int): integer called k
        Returns:
            int: kth number in array of nums
        Examples:
            nums = [3,2,5,4,1] k = 2 <- 4
            nums = [1,4,4,3,2,3] k = 4 <- 3
        """
        nums.sort()
        return nums[-k]

# heap
# n = len(nums)
# time = O(nlog k)
# space = O(k)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Args:
            nums (List[int]): integer array called nums
            k (int): integer called k
        Returns:
            int: kth number in array of nums
        Examples:
            nums = [3,2,5,4,1] k = 2 <- 4
            nums = [1,4,4,3,2,3] k = 4 <- 3
        """
        if not nums:
            return None
            
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap,num)
            else:
                heapq.heappushpop(heap,num)
        return heap[0]