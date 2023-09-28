"""
Time complexity: O(n)
Space complexity: O(n) - call stack
Thought Process:
- Perform dfs every time the program encounter a cell that is land, and keep track of maximum area
"""
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        # Helper function
        def dfs(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == 0:
                return 0
            # If the cell is land, add to visited set
            visited.add((row, col))
            # Add to total area
            return 1 + dfs(row + 1, col) + dfs(row, col + 1) + dfs(row - 1, col) + dfs(row, col - 1)
        
        # Iterate through the whole matrix, and perform dfs whenever land is found
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    temp = dfs(row, col)
                    if temp > maxArea:
                        maxArea = temp
        return maxArea
            
        