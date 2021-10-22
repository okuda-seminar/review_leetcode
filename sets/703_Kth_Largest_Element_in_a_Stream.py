# n = len(nums)
# time = O(1)
# space = O(n)
import heapq
class KthLargest:
    """compute K th largest element"""
    def __init__(self, k: int, nums: List[int]):
        """
        Args:
            k (int): k is number of largest (1 <= k <= 10^4)
            nums (List[int]): nums is list of integer array (0 <= nums.length <= 10^4, -10^4 <= nums[i] <= 10^4)
        Returns:
            null
        """
        assert type(k) == int, "type of k should be integer"
        assert type(nums) == list, "type of nums should be list"
        if k < 1 or 10**4 < k:
            raise ValueError("input is out of range")
        if len(nums) < 0 or 10**4 < len(nums):
            raise ValueError("input is out of range")
        self.k = k
        self.heap = []
        for num in nums:
            assert type(num) == int, "type of num is integer"
            if num < -10**4 or 10**4 < num:
                raise ValueError("input is out of range")
            if len(self.heap) < self.k:
                heapq.heappush(self.heap,num)
            else:
                if self.heap[0] < num:
                    heapq.heappushpop(self.heap,num)
    def add(self, val: int) -> int:
        """
        Args:
            val (int): add integer in list of nums (-10^4 <= val <= 10^4)
        Returns:
            int: k th largest integer 
        """
        assert type(val) == int, "type of val should be integer"
        if -10**4 > val or 10**4 < val:
            raise ValueError("input is out of range")
            
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
        else:
            if self.heap[0] < val:
                heapq.heappushpop(self.heap,val)
        return self.heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)