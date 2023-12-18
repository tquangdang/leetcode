from typing import List 
"""
Time complexity: O(n)
Space complexity: O(n)
Thought process:
- Since the time threshold is O(n), it is natural for me to think of using more space to reduce time complexity.
- A set is being use here for constant lookup time (can reduce the time to count the sequences)
- First, add all the numbers into the set. That way, we can eliminate duplicates
- Second, loop through the number list, and see if the current number we are at is the start of the sequence. 
        + If yes start counting upward
        + If not, skip that number and go to the next one
    By doing this, the time taken to solve a huge number of elements will be dramatically reduced
- Finally, repeatedly compare the current consecutive length with the maximum we currently got
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge cases, where the array is empty
        if len(nums) < 2:
            return len(nums)
        # Create a set, and add all the numbers to it
        setNums = set(nums)
        # Initialize a result variable, and a temp variable
        result, temp = 1, 1
        for num in nums:
            # Check if it's the  start of the sequence
            if num - 1 not in setNums:
                # Reepeatedly count up
                while num + 1 in setNums:
                    temp += 1
                    num += 1
                result = max(result, temp)
                temp = 1
        return result