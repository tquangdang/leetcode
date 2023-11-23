"""
Time complexity: O(n)
Space complexity: O(n)
Thought process: 
- Since we cannot use division operation, the brute force idea would be to calculate an element's prefix and postfix product. 
    To do this, we can create 2 seperate array (prefix and postfix), and iterate through the input array twice to complete them.
- However, we can do that directly in the result array (which does not count in the space complexity)
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a result array with the size of len(nums)
        result = [1] * len(nums)

        # Iterate through the prefix
        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
        
        # Iterate through the postfix
        postfix = 1
        # Iterate backward
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result