from typing import List 
"""
Time complexity: O(n)
Space complexity: O(1) - only 2 pointers were created
Thought process:
- We can use two pointers method to control the current sum. Since the list is sorted, 
  we can increase the sum by moving the start pointer forward, and decrease the sum 
  by moving the end pointer backward
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize 2 pointers at the beginning and end of the array
        start, end = 0, len(numbers) - 1
        
        # Loop through the array
        while start < end:
            # Calculate the total
            total = numbers[start] + numbers[end]
            # Increase the total if it's smaller than the target
            if total < target:
                start += 1
            # Else, decrease the total
            elif total > target:
                end -= 1
            # If the target is found:
            else:
                return [start + 1, end + 1]