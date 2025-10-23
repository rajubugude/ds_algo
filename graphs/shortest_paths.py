from collections import deque
from typing import List, Tuple
from sortedcontainers import SortedSet
import heapq
#TODO : NOTE However, heapq.heappush(pq, (dx, dy, length + 1)) does not ensure proper
#  ordering because Python's heapq orders elements by the first element of the tuple.

# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
class Solution:
    def shortestPath(self, adj, src):
        # code here
        n = len(adj)
        ans = [-1]*n
        vis  = [0]*n
        queue = deque()
        queue.append((src, 0))
        vis[src] = 1
        ans[src] = 0
        while queue:
            node, length = queue.popleft()
            ans[node] = length
            for adj_node in adj[node]:
                if not vis[adj_node]:
                    queue.append((adj_node, length+1))
                    vis[adj_node] = 1
        return ans
    

# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
class Solution:
    def topoSort(self, node, vis, st, adj):
        vis[node] = True
        for v, wt in adj[node]:
            if not vis[v]:
                self.topoSort(v, vis, st, adj)
        st.append(node)

    def shortestPath(self, N, M, edges):
        adj = [[] for _ in range(N)]
        for u, v, wt in edges:
            adj[u].append((v, wt))

        # Step 1: Topological Sort using DFS
        vis = [False] * N
        st = []
        for i in range(N):
            if not vis[i]:
                self.topoSort(i, vis, st, adj)

        # Step 2: Initialize distances
        dist = [-1] * N
        dist[0] = 0

        # Step 3: Process nodes in topological order
        while st:
            node = st.pop()  # Get node from topological order stack
            if dist[node] != -1: 
                #this is to ensure, from src will start the process of relaxing
                for v, wt in adj[node]:
                    if dist[v] == -1 or dist[node] + wt < dist[v]:
                        dist[v] = dist[node] + wt
        return dist
        

#TODO - Dijsktra's Algorithm using PQ

#Limitaions -> won't work with graphs having negative edge weights and negative cycles

# Time Complexity : O( E log(V) ) 
# Where E = Number of edges and V = Number of Nodes.
# Space Complexity : O( |E| + |V| ) 
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


#using set in python
class Solution:
    def dijkstra(self, V: int, adj: List[List[Tuple[int, int]]], S: int) -> List[int]:
        """
        Implements Dijkstra's algorithm using a SortedSet (similar to C++ set).

        :param V: Number of vertices in the graph.
        :param adj: Adjacency list where adj[i] contains (neighbor, edge_weight).
        :param S: Source vertex.
        :return: List containing shortest distances from S to all nodes.
        """
        # SortedSet will store (distance, node), automatically sorting by distance
        st = SortedSet()
        
        # Distance array initialized to a large value (infinity)
        dist = [float('inf')] * V
        dist[S] = 0
        
        # Insert the source node with distance 0
        st.add((0, S))  # (distance, node)
        
        while st:
            # Get the node with the smallest distance
            dis, node = st.pop(0)  # Removes the smallest element
            
            # Traverse all adjacent nodes
            for adjNode, edgeWeight in adj[node]:
                if dis + edgeWeight < dist[adjNode]:
                    # If the node was previously in the set with a higher distance, remove it
                    if dist[adjNode] != float('inf'):
                        st.discard((dist[adjNode], adjNode))
                    
                    # Update distance and add it to the set
                    dist[adjNode] = dis + edgeWeight
                    st.add((dist[adjNode], adjNode))
        
        return dist


# Example Usage
edges = [
    (0, 1, 4),
    (0, 2, 1),
    (2, 1, 2),
    (1, 3, 1),
    (2, 3, 5)
]
n = 4  # Number of nodes
src = 0
sol = Solution()
print(sol.dijkstra(n, edges, src))  # Output: [0, 3, 1, 4]

l = [float('-inf')] * 4
print(l)



# https://leetcode.com/problems/shortest-path-in-binary-matrix/
directions = [[0,1], [0,-1], [1,0], [-1,0], [1,1], [1,-1], [-1,1], [-1,-1]]
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        vis = [[0] * n for _ in range(n)]
        vis[0][0] = 1
        return self.bfs(0, 0, grid, n, vis)
    
    def bfs(self, x, y, grid, n, vis):
        pq = []
        heapq.heappush(pq, (1, x, y))
        while pq:
            length, u, v = heapq.heappop(pq)
            if u == n-1 and v == n-1:
                return length
            for du, dv in directions:
                dx = u + du
                dy = v + dv
                if 0 <= dx < n and 0 <= dy < n and grid[dx][dy] == 0 \
                 and not vis[dx][dy]:
                    heapq.heappush(pq, (length + 1, dx, dy))
                    vis[dx][dy] = 1
        return -1  


# https://leetcode.com/problems/path-with-minimum-effort/
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dist = [[float('inf') for _ in range(cols)] for _ in range(rows)]
        dist[0][0] = 0
        minHeap = [] 
        heapq.heappush(minHeap, (0,0,0))
        
        while minHeap:
            effort, x, y = heapq.heappop(minHeap)

            if x == rows - 1 and y == cols - 1:
                return effort
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < rows and 0 <= ny < cols:
                    abs_diff = abs(heights[x][y] - heights[nx][ny])
                    new_effort = max(effort, abs_diff)
                    
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(minHeap, (new_effort, nx, ny))


# https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, wt in flights:
            adj[u].append((v, wt))
        
        pq = [(0, 0, src)]  # (cost, stops, node)
        dist = {}  # Dictionary to track the minimum cost for a given (node, stops)

        while pq:
            cost, stops, node = heapq.heappop(pq)

            if node == dst:
                return cost

            if stops > k:
                continue
            
            for neighbor, price in adj[node]:
                new_cost = cost + price
                # Only proceed if this path has fewer stops and is cheaper
                if (neighbor, stops) not in dist or \
                        new_cost < dist[(neighbor, stops)]:
                    dist[(neighbor, stops)] = new_cost
                    heapq.heappush(pq, (new_cost, stops + 1, neighbor))

        return -1


# https://leetcode.com/problems/network-delay-time/
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, wt in times:
            u = u-1
            v = v-1
            adj[u].append((v, wt))

        dist = [float('inf')] * n
        dist[k-1] = 0

        pq = [(0, k-1)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, weight in adj[node]:
                new_dist = dist[node] + weight
                if new_dist < dist[neighbor]:  # Found a shorter path
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        maxi = float('-inf')
        for d in dist:
            if d == float('inf'):
                return -1
            maxi = max(maxi, d)
        return maxi
    

# https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description/
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        adj = [[] for _ in range(n)]
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        dist = [float('inf')] * n
        dist[0] = 0
        ways = [0] * n
        ways[0] = 1
        pq = []
        heapq.heappush(pq,(0,0)) # dist, node
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for adj_node, adj_d in adj[node]:
                curr_dist = adj_d + dist[node]
                if curr_dist < dist[adj_node]:
                    dist[adj_node] = curr_dist
                    ways[adj_node] = ways[node]
                    heapq.heappush(pq, (curr_dist, adj_node))

                elif curr_dist == dist[adj_node]:
                    ways[adj_node] += ways[node]
                    ways[adj_node] = ways[adj_node]%mod
        return ways[n-1]%mod
    


# https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1
class Solution:
    def minimumMultiplications(self, arr: List[int], start: int, end: int) -> int:
        # Edge case: if start is already equal to end
        if start == end:
            return 0

        # Create a queue for BFS traversal (stores (current_number, steps))
        q = deque([(start, 0)])

        # Distance array to store minimum multiplications required
        dist = [float('inf')] * 100000
        dist[start] = 0
        mod = 100000

        # BFS Traversal
        while q:
            node, steps = q.popleft()

            for num in arr:
                new_node = (node * num) % mod

                # If a shorter path to 'new_node' is found, update distance
                if steps + 1 < dist[new_node]:
                    dist[new_node] = steps + 1

                    # If we reach the end number, return the step count
                    if new_node == end:
                        return steps + 1

                    q.append((new_node, steps + 1))

        # If the end number is unreachable
        return -1

start = 3
end = 30
arr = [2, 5, 7]

obj = Solution()
ans = obj.minimumMultiplications(arr, start, end)
print(ans)


# Dijsktra's on 2D grid.
# https://leetcode.com/problems/find-minimum-time-to-reach-last-room-i/description/

class Solution:
    def minTimeToReach(self, moveTime):
        m, n = len(moveTime), len(moveTime[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]  # time, row, col

        while heap:
            time, r, c = heapq.heappop(heap)
            if (r, c) == (m-1, n-1):
                return time
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    wait_time = max(time, moveTime[nr][nc]) + 1
                    if wait_time < dist[nr][nc]:
                        dist[nr][nc] = wait_time
                        heapq.heappush(heap, (wait_time, nr, nc))
        return -1
