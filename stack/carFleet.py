'''
Time complexity: O(nlogn), from sorting 
Space complexity: O(n)
Thought process:
- To identify a fleet, it is necessary to think of them as graphs of the relationship between distance and time. The number of intersections are also the number of fleet.
- We will solve this problem by first sorting the input array in descending order
- Then, create a stack, and push into the stack the time needed to get to the destination of each car.
- If the current time is less that the time already in the stack, we know that there is a fleet consists of these two cars. We then pop the current time out of the stack
- Finally, return the length of the stack
'''
from typing import List 
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            pairs.append([position[i], speed[i]])
        # Sort in reverse
        pairs.sort(reverse = True)

        # Initialize a stack
        stack = []
        for pair in pairs:
            # Calculate the time, and push it to the stack
            stack.append((target - pair[0]) / pair[1])
            # If there are two or more elements in the stack, and the current one is smaller than the previous top of stack
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)