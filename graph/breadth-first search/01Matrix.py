"""
Time complexity: O(n) - visit each cell once
Space complexity: O(n) - size of the queue
Thought process:
- Treat 0s and 1s as layers of bfs algorithm. After each level, increment the distance to 1, and traverse to the next inner layer
- Traverse through the matrix, append all 0s to the queue, and replace all 1s with -1 (unvisited), then perform bfs
"""
from collections import deque
from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # Edge case
        if not mat:
            return mat
        
        # If not edge case
        rows = len(mat)
        cols = len(mat[0])
        # Create a queue to perform BFS later
        queue = deque()

        # Iterate through the matrix, add all coordinates of 0s into the queue, and mark all 1s as -1 (unvisited)
        for i in range(rows):
            for j in range(cols):
                # If encounter 0
                if mat[i][j] == 0:
                    queue.append([i, j])
                else:
                    mat[i][j] = -1
        # Perform BFS, layer by layer
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # Set initial distance to 1. It will increase after each level
        distance = 1
        # BFS
        while queue:
            size = len(queue)
            for i in range(size):
                temp = queue.popleft()
                x, y = temp[0], temp[1]
                for direction in directions:
                    row, col = x + direction[0], y + direction[1]
                    # Check if the cell is valid
                    if row >= 0 and row < rows and col >= 0 and col < cols and mat[row][col] == -1:
                        mat[row][col] = distance
                        # Add the current coordinate to the queue, to perform search on next layer
                        queue.append([row, col])
            # Increment distance after each level
            distance += 1
        return mat
