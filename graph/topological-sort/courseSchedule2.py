from typing import List 
from collections import defaultdict

'''
n: number of nodes (courses)
e: number of edges (connections)
Time complexity: O(n + e)
Space complexity: O(n + e)
Thought process:
- Topological sort: perform dfs on every node, and stop exploring whenever encountered a visited node
- A key thing to remember is the initialization of 2 sets, visited (to detect visited node) and visiting (to detect cycles). 
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Reconstruct the graph (adjacency list)
        graph = defaultdict(list)
        for course in prerequisites:
            graph[course[0]].append(course[1])

        result = []
        
        # Initialize 2 hashset, visited and visiting (visiting is used to detect cycle)
        visited, visiting = set(), set()
        # DFS helper function that performs topological sort
        def dfs(node):
            # Base case (if cycle is detected or current node is already visited)
            if node in visited:
                return True
            if node in visiting:
                return False
            # If not base case, add the current node to visiting set
            visiting.add(node)
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visiting.remove(node)
            visited.add(node)
            result.append(node)
            return True
        
        # Perform dfs on every node
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result