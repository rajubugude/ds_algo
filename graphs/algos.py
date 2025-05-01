import heapq
from collections import deque
from typing import List, Tuple

# https://www.geeksforgeeks.org/problems/topological-sort/1
#TC: O(V+E), SC: O(V)

'''
Topological sorting only exists in Directed Acyclic Graph (DAG). 
If the nodes of a graph are connected through directed edges and the graph does 
    not contain a cycle, it is called a directed acyclic graph(DAG). 

The topological sorting of a directed acyclic graph is nothing but the linear ordering
 of vertices such that if there is an edge between node u and v(u -> v), 
 node u appears before v in that ordering.
'''

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
        ans.append(node) #append after completing the dfs for a node, to toposort.


#topo sort BFS - khan's Algo
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




#TODO - Dijsktra's Algorithm using PQ

#Limitaions -> won't work with graphs having negative edge weights and negative cycles
# Negative Cycle: A cycle is called a negative cycle if the sum of all its weights becomes negative. 

# Time Complexity : O( E log(V) ) 
# Where E = Number of edges and V = Number of Nodes.
# Space Complexity : O( E + V ) 
# Where E = Number of edges and V = Number of Nodes.

class Solution:
    def dijkstra(self, n, edges, src):
        # Step 1: Build adjacency list (graph)
        adj = [[] for _ in range(n)]
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))  # Undirected Graph

        # Step 2: Initialize distance array
        dist = [float('inf')] * n
        dist[src] = 0

        # Step 3: Min-Heap (priority queue) → (distance, node)
        pq = []  # (distance, node)
        heapq.heappush(pq,(0,src))
        
        while pq:
            #Note: ele with shortest d, comes first, if d is same, then node with less val comes first
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            # Step 4: Relaxation step
            for neighbor, weight in adj[node]:
                new_dist = dist[node] + weight
                if new_dist < dist[neighbor]:  # Found a shorter path
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        # Replace 'inf' with -1 for unreachable nodes
        return [-1 if x == float('inf') else x for x in dist]



#TODO - BellmanFord Algo - Same as Dijsktra's
# To find shortest path from one source to all other edges. Works in Directed Graphs only
#if given graph is undirected, u -- v, then convert it to u --> v and v --> u.

#Advantages -> Helps to detect in negative cycles as well.

#Algo -> relax all the edges n-1 time sequentially(n is number of nodes).
    #At nth iteration, if relaxation is done, then it has negative cycle   

# TC : O(V X E) , V - no of node, E - no of edges (quadratic)
#SC : O(V) for dist array
class Solution:
    '''
    n: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    '''
    def bellmanFord(self, n, edges, src):
        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        for _ in range(n-1):
            for u, v, wt in edges:
                curr_dist =  dist[u] + wt
                if dist[v] > curr_dist:
                    dist[v] = curr_dist
                    
        #At nth iteration, if relaxation is done, then it has negative cycle            
        for u, v, wt in edges:
            if dist[u] + wt < dist[v]:
                return [-1]
        
        for i in range(n):
            if dist[i] == float('inf'):
                dist[i]=10**8
            
        return dist
    


# Spanning Tree:
# A spanning tree is a tree in which we have N nodes(i.e. All the nodes present in the original graph)
#     and N-1 edges and all nodes are reachable from each other.

# Minimum Spanning Tree:
# Among all possible spanning trees of a graph, the minimum spanning tree is the one for which 
#     the sum of all the edge weights is the minimum.


#Prim's Algo

# Time Complexity: O(E*logE) + O(E*logE)~ O(E*logE), where E = no. of given edges.
# Space Complexity: O(E) + O(V), where E = no. of edges and V = no. of vertices. 
import heapq
class Solution:
    def min_spanning_tree(self, n: int, adj) -> int:
        vis = [0] * n
        pq = []
        res = 0  # to store MST weight sum
        # heapq.heappush(pq, (0, 0, -1))  # (weight, node, parent)
        heapq.heappush(pq, (0, 0))  # (weight, node)

        while pq:
            wt, node = heapq.heappop(pq)
            if vis[node]:
                continue
            vis[node] = 1  # Mark node as visited
            res += wt

            for adj_node, adj_wt in adj[node]:
                if not vis[adj_node]:
                    heapq.heappush(pq, (adj_wt, adj_node))

        return res