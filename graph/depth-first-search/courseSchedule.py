"""
Time complexity: O(m + n) - with n and m being the total number of nodes and edges
Space complexity: O(m + n) 
Thought process:
- Reconstruct the graph as an adjacency list
- Perform dfs from every node to find cycle, and return the result afterward
"""
from typing import List
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Reconstruct the graph, turn it into an adjacency list
        graph = defaultdict(list)
        for course in prerequisites:
            graph[course[1]].append(course[0])
        # Create a visited set to detect cycles
        visited = set()

        # Helper function to perform dfs on a course
        def dfs(course):
            # Base cases
            if course in visited:
                return False
            if graph[course] == []:
                return True

            # If not base case,
            visited.add(course)
            for neighbor in graph[course]:
                # If a cycle is detected
                if dfs(neighbor) == False:
                    return False
            # If no cycle is detected, this means the course can be taken
            visited.remove(course)
            graph[course] = []
            return True

        # Perform dfs, starting from every nodes, in case the graph is disconnected
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True