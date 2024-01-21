"""
Time Complexity: O(n^2)
Space Complexity: O(n)
Thought Process:
- The optimized way to solve this problem is from the problem "Two Sums 2- Input Array Is Sorted".
- First, sort the array.
- Then, starting from the first number, we solve it using 2 pointers method , with the window range from the second element to the last.
- To avoid duplicates, we do not want to start with the same number again, both in the outer loop and the inner 2 pointers loop.
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Sort the input array
        nums.sort()
        # Loop through the input array
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 2 pointers method
            start, end = i + 1, len(nums) - 1
            while start < end:
                if nums[i] + nums[start] + nums[end] > 0:
                    end -= 1
                elif nums[i] + nums[start] + nums[end] < 0:
                    start += 1
                else:
                    result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        return result