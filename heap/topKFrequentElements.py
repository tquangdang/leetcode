"""
Time complexity: O(nlog(k)), since building the hashtable take O(n), and pushing n elements into a heap size k take O(nlogk).
Space complexity: O(n + k)
Thought process:
- In this problem, we would want to use a min heap, intuitivelly. When popping elements out of a min heap,  we always know that the element is the smallest among current elements.
- Use a min heap of size k, and add elements to it in the format of [frequency, element], so that the heap will be sorted based on frequency.
- Pop an element out whenever the length of the heap exceed size k, to keep the top K frequent elements.
"""
from typing import List 
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a hashmap, with the key being the number, and the value being the frequency
        dict = {}
        result = []
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
        # Create a heap (Python heap is a min-heap by default)
        heap = []
        # Make it a min heap of size k by popping elements when the length exceed k
        for key, value in dict.items():
            heappush(heap, [value, key])
            if len(heap) > k:
                heappop(heap)
        # The remaining elements will be the desired result
        for i in range(k):
            result.append(heappop(heap)[1])
        return result