"""
Time complexity: O(n)
Space complexity: O(n) - call stack
Thought process:
- Since the land will be adjacent to each other, we can perform dfs until we can't anymore, and increment the island count
"""
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        # Helper function to find an island
        def dfs(row, col):
            # If land is out of bound, or not land 
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return
            # Else: mark that island to be 0, and keep going in 4 directions
            grid[row][col] = "0" 
            dfs(row - 1, col)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row , col + 1)
        # Scan through the grid until we see an island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    result += 1
        return result