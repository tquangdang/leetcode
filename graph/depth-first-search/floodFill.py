"""
Time complexity: O(n)
Space complexity: O(n) - call stack
Thought process:
- Perform dfs on the targeted pixel to fill them.
- The important part is to set the condition of the recursion call
"""
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Keep a visited set 
        visited = set()
        startingColor = image[sr][sc]
        def dfs (row, col):
            # Conditions that will stop the recursion
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != startingColor or (row, col) in visited:
                return
            # Else, add the current coordinate to visited
            visited.add((row, col))
            # Fill it to the desired color
            image[row][col] = color
            # Keep filling to adjacent part of the matrix
            dfs(row + 1, col)
            dfs(row , col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)
        dfs(sr, sc)
        return image