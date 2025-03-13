'''
Topological sorting only exists in Directed Acyclic Graph (DAG). 
If the nodes of a graph are connected through directed edges and the graph does 
    not contain a cycle, it is called a directed acyclic graph(DAG). 

The topological sorting of a directed acyclic graph is nothing but the linear ordering
 of vertices such that if there is an edge between node u and v(u -> v), 
 node u appears before v in that ordering.
'''

from collections import deque
from typing import List

# https://www.geeksforgeeks.org/problems/topological-sort/1
#TC: O(V+E), SC: O(V)

#topo sort DFS
class Solution:
    def topologicalSort_dfs(self,adj):
        n = len(adj)
        vis = [0] * n
        ans = []
        for node in range(n):
            if not vis[node]:
                self.dfs(node, vis, adj, ans)
        return ans[::-1]
    
    def dfs(self, node, vis, adj, ans):
        vis[node] = 1
        for adj_node in adj[node]:
            if not vis[adj_node]:
                self.dfs(adj_node, vis, adj, ans)
        ans.append(node)


#topo sort BFS
class Solution:
    def topologicalSort_bfs(self,adj):
        n = len(adj)
        ans = []
        queue = deque()
        indegree = [0]*n
        for node in range(n):
            for adj_node in adj[node]:
                indegree[adj_node] += 1
        
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        if not queue:
            return []
        
        return self.bfs(adj, indegree, ans, queue)
    
    def bfs(self, adj, indegree, ans, queue):
        while queue:
            curr_node = queue.popleft()
            ans.append(curr_node)
            for adj_node in adj[curr_node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        return ans         
    
# adj = [[], [], [3], [1], [0, 1], [0, 2]]

# s = Solution()
# print(s.topologicalSort(adj))


# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
class Solution:
    # Function to detect cycle in a directed graph.
    def isCyclic(self, adj: List[List[int]]) -> bool:
        n = len(adj)
        queue = deque()
        indegree = [0] * n
        count = 0
        
        # Compute in-degree for each node
        for node in range(n):
            for adj_node in adj[node]:
                indegree[adj_node] += 1
        
        # Add nodes with in-degree 0 to queue
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        
        # Call BFS and get the processed count
        count = self.bfs(adj, indegree, queue)
        
        # If all nodes were processed, there is no cycle; otherwise, there is a cycle
        return count != n
    
    def bfs(self, adj, indegree, queue):
        count = 0  # Define count locally
        while queue:
            curr_node = queue.popleft()
            count += 1
            for adj_node in adj[curr_node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)
        return count