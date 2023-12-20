'''
Time complexity: O(logn)
Space complexity: O(1)
Thought process:
- In this problem, since the time constraint is O(logn), a solution related to binary search should be used. 
- We start searching from start to end, and there are three scenarios that can happen:
        + If the start element is smaller than the end element, we know for sure that the current window is sorted
        + If the middle element is larger then the start element, we know that we are in the sorted bigger part of the array, and the result won't be there. So we update the start pointer to mid + 1
        + If the middle element is smaller than the start element, we know that the middle could be the pivot point (which could also be the result), and to keep searching for the correct pivot point/make sure the current one is correct, we don't want to keep searching in the later half. The end pointer will be updated to mid - 1.
    * Update the result accordingly in each step is necessary
'''
from typing import List 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        start, end = 0, len(nums) - 1
        while start <= end:
            # If sorted:
            if nums[start] < nums[end]:
                result = min(result, nums[start])
                break
            # If not sorted
            mid = (start + end) // 2
            result = min(result, nums[mid])
            if nums[mid] >= nums[start]:
                start = mid + 1
            else:
                end = mid - 1
        return result
    