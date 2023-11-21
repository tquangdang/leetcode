from heapq import heappush, heappop, heapify
from typing import List
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # Initialize integer k and an integer list nums (Python default is min heap)
        self.k = k
        self.nums = nums
        heapify(nums)
        # Maintain a min heap of size k by popping out elements that make the size larger than k
        while len(self.nums) > k:
            heappop(self.nums)
        
    def add(self, val: int) -> int:
        # Push the integer into the heap
        heappush(self.nums, val)
        # Maintain the heap size (k)
        if len(self.nums) > self.k:
            heappop(self.nums)
        # The result will be the top of the min heap
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)