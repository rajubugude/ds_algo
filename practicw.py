# from collections import deque
# def isBipartite(graph) -> bool:
#     n = len(graph)
#     color = [0] * n
#     for node in range(n):
#         if not color[node]:
#             if not bfs(node, color, graph):
#                 return False
#     return True
#
# def bfs(node, color, graph):
#     queue = deque([node])
#     color[node] = 1
#     while queue:
#         curr = queue.popleft()
#         for adj_node in graph[curr]:
#             if color[adj_node] == 0:
#                 color[adj_node] = 3 - color[curr]
#                 queue.append(adj_node)
#             elif color[adj_node] == color[curr]:
#                 return False
#     return True
#
# graph = [[1,3],[0,2],[1,3],[0,2]]
# print(isBipartite(graph))

# from collections import deque
#
# class Solution:
#     def isCycle(self, n, edges):
#         adj = [[] for _ in range(n)]
#         for u, v in edges:
#             adj[u].append(v)
#             adj[v].append(u)
#
#         vis = [0] * n
#         for node in range(n):
#             if not vis[node]:
#                 if self.bfs(node, adj, vis):
#                     return True
#         return False
#
#     def bfs(self, node, adj, vis):
#         queue = deque()
#         queue.append((node, -1))
#         vis[node] = 1
#         while queue:
#             curr_node, parent = queue.popleft()
#             for adj_node in adj[curr_node]:
#                 if not vis[adj_node]:
#                     vis[adj_node] = 1
#                     queue.append((adj_node, curr_node))
#                 else:
#                     if parent != adj_node:
#                         return True
#         return False
#
# edges = [[0,2],[0,1],[1,2]]
# s = Solution()
# print(s.isCycle(3, edges))


from typing import  List
# class Solution:
#     def findCircleNum(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#         ans = 0
#         vis = [[0]*n for _ in range(n)]
#         direc = [0, 1, 0, -1, 0]
#         for i in range(n):
#             for j in range(n):
#                 if i != j and grid[i][j] and not vis[i][j]:
#                     self.dfs(i, j, n, vis, grid, direc)
#                     ans += 1
#         return ans
#
#     def dfs(self, row, col, n, vis, grid, direc):
#         if row < 0 or row >= n or col < 0 or col >= n or vis[row][col] or not grid[row][col] or row == col:
#             return
#
#         vis[row][col] = 1
#
#         for k in range(4):
#             nr = direc[k] + row
#             nc = direc[k+1] + col
#             self.dfs(nr, nc, n, vis, grid, direc)
#
# s = Solution()
# isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# print(s.findCircleNum(isConnected))



# from typing import List
# import heapq
# class Solution:
#     def spanningTree(self, n: int, adj: List[List[int]]) -> int:
#         pq = []
#         vis = [0] * n
#         res = 0
#         heapq.heappush(pq, (0,0, -1)) # wt, node
#         mst = []
#         while pq:
#             wt, node, parent = heapq.heappop(pq)
#             if vis[node]:
#                 continue
#
#             if parent != -1:
#                 mst.append([node, parent])
#
#             vis[node] = 1
#             res += wt
#
#             for adj_node, adj_wt in adj[node]:
#                 if not vis[adj_node]:
#                     heapq.heappush(pq, (adj_wt,adj_node, node))
#         print(mst)
#         return res
#
# s = Solution()
# adj = [[[1,2], [3,6]], [[0,2], [3,8], [4,5], [2,3]], [[1,3], [4,7]], [[0,6], [1,8]], [[1,5], [2,7]]]
# print(s.spanningTree(5, adj))

class DisjointSet:
    def __init__(self, n):
        self.parent  = [i for i in range(n)]
        self.rank = [0] * (n)

    def find_up(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_up(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ulp_u = self.find_up(u)
        ulp_v = self.find_up(v)
        if ulp_v == ulp_u:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_u] > self.rank[ulp_v]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

# from collections import defaultdict
# from typing import List
# import heapq
# class Solution:
#     def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
#         ds = DisjointSet(c)
#         for u, v in connections:
#             ds.union(u, v)
#
#
#         groups = defaultdict(list)
#         print(ds.parent)
#         for station in range(1, c + 1):
#             root = ds.find_up(station)
#             heapq.heappush(groups[root], station)
#
#         print(groups)
#         online = [1] * (c + 1)
#         ans = []
#         for a, b in queries:
#             if a == 2:
#                 online[b] = 0
#             else:
#                 if online[b]:
#                     ans.append(b)
#                 else:
#                     root = ds.find_up(b)
#                     group = groups[root]
#                     while group and not online[group[0]]:
#                         heapq.heappop(group)
#                     if group:
#                         ans.append(group[0])
#                     else:
#                         ans.append(-1)
#                 print(groups, ans)
#         return ans
#
# c = 6
# connections = [[1,2],[1,3],[3,4],[5,6]]
# queries = [[1,3],[2,1],[1,1],[1,6],[2,6],[2,3],[1,3], [1,6]]
# s = Solution()
# print(s.processQueries(c, connections, queries))

# class Solution:
#     def spanningTree(self, n: int, adj: List[List[int]]) -> int:
#         vis = [0] * n
#         edges = []
#         for node in range(n):
#             adj_list = adj[node]
#             for v, wt in adj_list:
#                 edges.append((wt, (node,v)))
#         edges.sort()
#         mst = []
#         print(edges)
#         ds = DisjointSet(n)
#         res = 0
#         for edge in edges:
#             wt = edge[0]
#             u = edge[1][0]
#             v = edge[1][1]
#             print(ds.parent)
#             if ds.find_up(u) != ds.find_up(v):
#                 res += wt
#                 ds.union(u, v)
#                 mst.append([u,v])
#         print(mst)
#         return res
#
#
# s = Solution()
# adj = [[[1,2], [3,6]], [[0,2], [3,8], [4,5], [2,3]], [[1,3], [4,7]], [[0,6], [1,8]], [[1,5], [2,7]]]
# print(s.spanningTree(5, adj))


# class Solution:
#     def removeStones(self, stones: List[List[int]]) -> int:
#         n = len(stones)
#         ds = DisjointSet(n)
#         count = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
#                     # print(stones[i][0], stones[j][0])
#                     # print(stones[i][1], stones[j][1])
#                     count += 1
#                     print(i,j, end=', here ')
#             print()
#         print('here')
#         return count
# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# s = Solution()
# print(s.removeStones(stones))

# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         n = len(nums)
#         s = 0
#         e = n-1
#         while s <= e:
#             mid = (s+e)//2
#             if mid > 0 and mid < n-1:
#                 if nums[mid+1] != nums[mid] and nums[mid] != nums[mid-1]:
#                     return nums[mid]
#             elif mid == 0:
#                 if nums[mid] != nums[mid+1]:
#                     return nums[mid]
#             elif mid == n-1:
#                 if nums[mid] != nums[mid-1]:
#                     return nums[mid]
#             s = mid+1
#
#         s = 0
#         e = n-1
#         while s <= e:
#             mid = (s+e)//2
#             if mid > 0 and mid < n-1:
#                 if nums[mid+1] != nums[mid] and nums[mid] != nums[mid-1]:
#                     return nums[mid]
#             elif mid == 0:
#                 if nums[mid] != nums[mid+1]:
#                     return nums[mid]
#             elif mid == n-1:
#                 if nums[mid] != nums[mid-1]:
#                     return nums[mid]
#             e = mid-1
#
#         return -1
#
# s = Solution()
# nums = [1,1,2,3,3,4,4,8,8]
# print(s.singleNonDuplicate(nums))


# from typing import List
# from collections import defaultdict
# import heapq
#
#
# class Solution:
#     def minMoves(self, matrix: List[str]) -> int:
#         m, n = len(matrix), len(matrix[0])
#         portals = defaultdict(list)
#         used_portals = set()
#         visited = [[False] * n for _ in range(m)]
#
#         # Collect portal positions
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] not in ('.', '#'):
#                     portals[matrix[i][j]].append((i, j))
#
#         # Min-heap for Dijkstra's algorithm
#         pq = [(0, 0, 0)]  # (distance, x, y)
#
#         directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#         while pq:
#             dist, x, y = heapq.heappop(pq)
#
#             if (x, y) == (m - 1, n - 1):
#                 return dist
#
#             if visited[x][y]:
#                 continue
#             visited[x][y] = True
#
#             # Move to adjacent cells
#             for dx, dy in directions:
#                 nx, ny = x + dx, y + dy
#                 if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] != '#':
#                     heapq.heappush(pq, (dist + 1, nx, ny))
#
#             # Teleportation
#             cell = matrix[x][y]
#             if cell not in ('.', '#') and cell not in used_portals:
#                 for tx, ty in portals[cell]:
#                     if not visited[tx][ty]:
#                         heapq.heappush(pq, (dist, tx, ty))
#                 used_portals.add(cell)
#
#         return -1
#
#
# matrix = ["A..","..A","A..","..."]
# s = Solution()
# print(s.minMoves(matrix))


# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [1] * n
#         prev = [-1] * n
#
#         for idx in range(n):
#             for prev_idx in range(idx):
#                 if nums[prev_idx] < nums[idx] and dp[idx] < 1 + dp[prev_idx]:
#                     dp[idx] = 1 + dp[prev_idx]
#                     prev[idx] = prev_idx
#
#         maxi = max(dp)
#         last_idx = dp.index(maxi)
#
#         # Reconstruct the LIS
#         res = []
#         while last_idx != -1:
#             res.append(nums[last_idx])
#             last_idx = prev[last_idx]
#
#         print("LIS:", res[::-1])
#         return maxi
#
# s = Solution()
# nums = [10,9,2,5,3,7,101,18]
# print(s.lengthOfLIS(nums))

from collections import deque

def to_xy(s: str):
    x = ord(s[0]) - ord('a')
    y = int(s[1]) - 1
    return x, y

def knight_min_moves(src, dst, n=8):
    sx, sy = src
    dx, dy = dst
    if (sx, sy) == (dx, dy):
        return 0

    moves = [(-2, 1), (-2, -1), (2, -1), (2, 1),
             (1, -2), (1,  2), (-1, -2), (-1,  2)]

    # Use row-major indexing: vis[y][x]
    vis = [[False] * n for _ in range(n)]
    q = deque([(sx, sy, 0)])
    vis[sy][sx] = True

    while q:
        x, y, steps = q.popleft()
        for dxm, dym in moves:
            nx, ny = x + dxm, y + dym
            if 0 <= nx < n and 0 <= ny < n and not vis[ny][nx]:
                if (nx, ny) == (dx, dy):
                    return steps + 1
                vis[ny][nx] = True
                q.append((nx, ny, steps + 1))
    return -1

def main():
    t = int(input())
    for _ in range(t):
        s1, s2 = input().split()
        print(knight_min_moves(to_xy(s1), to_xy(s2)))

main()



