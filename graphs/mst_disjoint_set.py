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
    
# MST array(optional): If we wish to store the minimum spanning tree(MST) of the graph,
#    we need this array. This will store the edge information as a pair of starting and ending nodes of a particular edge.
    def spanningTree(self, n: int, adj) -> int:
        vis = [0] * n
        pq = []
        heapq.heappush(pq, (0, 0, -1))  # (weight, node, parent)
        mst = [] # to store the mstree
        res = 0
        while pq:
            wt, node, parent = heapq.heappop(pq)
            if vis[node]:
                continue
            vis[node] = 1  # Mark node as visited
            res += wt
            mst.append((node, parent))
            for adj_node, adj_wt in adj[node]:
                if not vis[adj_node]:
                    heapq.heappush(pq, (adj_wt, adj_node, node))

        return mst, res        



#Disjoint Set - Union by rank/size
# Time Complexity:  The time complexity is O(4) which is very small and close to 1. 
#   So, we can consider 4 as a constant.

class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def findUPar(self, node): #find ultimate parent, which is the top guy.
        if node == self.parent[node]:
            return node
        # Path compression
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return

        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return

        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]



ds1 = DisjointSet(7)
ds2 = DisjointSet(7)
# ds1.unionBySize(1, 2)
# ds1.unionBySize(2, 3)
# ds1.unionBySize(4, 5)
# ds1.unionBySize(6, 7)
# ds1.unionBySize(5, 6)

ds2.unionByRank(1, 2)
ds2.unionByRank(2, 3)
ds2.unionByRank(4, 5)
ds2.unionByRank(6, 7)
ds2.unionByRank(5, 6)

# Check if 3 and 7 are in the same set
if ds1.findUPar(3) == ds1.findUPar(7):
    print("Same")
else:
    print("Not same")

ds1.unionBySize(3, 7)

if ds2.findUPar(3) == ds2.findUPar(7):
    print("Same")
else:
    print("Not same")



# Kruskal'S Algo

# Time Complexity: O(N+E) + O(E logE) + O(E*4α*2)   where N = no. of nodes and E = no. of edges. 
#   O(N+E) for extracting edge information from the adjacency list. 
#   O(E logE) for sorting the array consists of the edge tuples. 
#   Finally, we are using the disjoint set operations inside a loop. 
#       The loop will continue to E times. Inside that loop, there are two disjoint set operations like findUPar() and UnionBySize() each taking 4 and so it will result in 4*2. 
#       That is why the last term O(E*4*2) is added.

# Space Complexity: O(N) + O(N) + O(E) where E = no. of edges and N = no. of nodes. 
#   O(E) space is taken by the array that we are using to store the edge information. 
#   And in the disjoint set data structure, we are using two N-sized arrays i.e. a parent
#    and a size array (as we are using unionBySize() function otherwise, 
#       a rank array of the same size if unionByRank() is used which result in the first two terms O(N).

# https://www.geeksforgeeks.org/problems/minimum-spanning-tree/1

from typing import List
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [0] * (n+1)
    
    def find_ulp(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find_ulp(self.parent[node])
        return self.parent[node]
    
    def union_by_size(self, u, v):
        ulp_u = self.find_ulp(u)
        ulp_v = self.find_ulp(v)
        
        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]     

class Solution:
    def spanningTree(self, n: int, adj: List[List[int]]) -> int:
        edges = []
        for u in range(n):
            for v_wt in adj[u]:
                v, wt = v_wt
                edges.append((wt, (u, v)))
        
        edges.sort()
        ds = DisjointSet(n)
        res = 0
        for edge in edges:
            wt = edge[0]
            u = edge[1][0]
            v = edge[1][1]
            if ds.find_ulp(u) != ds.find_ulp(v):
                res += wt
                ds.union_by_size(u, v)
        return res
    


# https://leetcode.com/problems/number-of-provinces/
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [0] * (n+1)
    
    def find_ulp(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find_ulp(self.parent[node])
        return self.parent[node]
    
    def union_by_size(self, u, v):
        ulp_u = self.find_ulp(u)
        ulp_v = self.find_ulp(v)
        
        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        ds = DisjointSet(n)
        for i in range(n):
            for j in range(n):
                if i != j and grid[i][j] == 1:
                    ds.union_by_size(i,j) #o based indexing only

        comp = 0
        for i in range(n):
            if ds.parent[i] == i:
                comp += 1
        return comp


# https://leetcode.com/problems/number-of-operations-to-make-network-connected/

#Brute force
# TC : O(V+E) DFS
#SC : O()
class Solution:
    def dfs(self,vertex,vis,adj):
        vis.add(vertex)
        for i in adj[vertex]:
            if i not in vis:
                self.dfs(i,vis,adj)
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges = len(connections)
        if edges < n - 1:
            return -1
        
        adj = [[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
            
        vis = set()
        count_components = 0
        for i in range(n):
            if i not in vis:
                self.dfs(i,vis,adj)
                count_components += 1
        return count_components-1
        
# Optimal - DSU
# Time Complexity: O(E*4α)+O(N*4α) where E = no. of edges and N = no. of nodes. 
#   The first term is to calculate the number of extra edges and the second term is to count the number of components. 
#   4α is for the disjoint set operation we have used and this term is so small that it can be considered constant.

# Space Complexity: O(2N) where N = no. of nodes. 
#   2N for the two arrays(parent and size) of size N we have used inside the disjoint set.

class DisjointSet:
    def __init__(self, n):
        self.size = [0] * (n)
        self.parent = [i for i in range(n)]
    
    def find_ulp(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ulp(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        ulp_u = self.find_ulp(u)
        ulp_v = self.find_ulp(v)

        if ulp_u == ulp_v:
            return 
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
         

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges = len(connections)
        if edges < n - 1:
            return -1

        ds = DisjointSet(n)
        extras = 0
        for u,v in connections:
            if ds.find_ulp(u) == ds.find_ulp(v):
                extras += 1
            else:
                ds.union_by_size(u, v)
        

        comp = 0
        for i in range(n):
            if ds.parent[i] == i:
                comp += 1
        ans = comp - 1

        return ans if extras >= ans else -1
              


# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

#Brute Force

    # IDEA 

    # ans = num of stones - num of connected comp
    # building graph - two nodes in same row/col forms an edge

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        adj = [[] for _ in range(n)] #create adj list , which are in same row/col

        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    adj[i].append(j)
                    adj[j].append(i)
        
        vis = [0] * n
        comp_count = 0
        for node in range(n):
            if not vis[node]:
                self.dfs(node, vis, adj)
                comp_count += 1
        return n - comp_count

    def dfs(self, node, vis, adj):
        vis[node] = 1
        for adj_node in adj[node]:
            if not vis[adj_node]:
                self.dfs(adj_node, vis, adj)
                          
# Optimal

# class DisjointSet:
#     def __init__(self, n):
#         self.parent = [i for i in range(n+1)]
#         self.size = [0] * (n+1)
    
#     def find_ulp(self, node):
#         if node == self.parent[node]:
#             return node
        
#         self.parent[node] = self.find_ulp(self.parent[node])
#         return self.parent[node]
    
#     def union_by_size(self, u, v):
#         ulp_u = self.find_ulp(u)
#         ulp_v = self.find_ulp(v)
        
#         if ulp_u == ulp_v:
#             return
        
#         if self.size[ulp_u] < self.size[ulp_v]:
#             self.parent[ulp_u] = ulp_v
#             self.size[ulp_v] += self.size[ulp_u]
#         else:
#             self.parent[ulp_v] = ulp_u
#             self.size[ulp_u] += self.size[ulp_v]
    
# class Solution:
#     # ans = num of stones - num of connected comp
#     # building graph - two nodes in same row/col forms an edge
#     def removeStones(self, stones: List[List[int]]) -> int:
#         n = len(stones)
#         ds = DisjointSet(n)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
#                     ds.union_by_size(i,j)
#         comp = 0
#         for i in range(n):
#             if ds.parent[i] == i:
#                 comp += 1
#         return n - comp  





# https://leetcode.com/problems/accounts-merge/

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [0] * (n+1)
    
    def find_ulp_node(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_ulp_node(self.parent[node])
        return self.parent[node]
    
    def union_by_size(self, u, v):
        ulp_u = self.find_ulp_node(u)
        ulp_v = self.find_ulp_node(v)

        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        map_email_idx = {}
        n = len(accounts)
        ds = DisjointSet(n)
        for i, account in enumerate(accounts):
            for mail in account[1:]:
                if mail not in map_email_idx:
                    map_email_idx[mail] = i
                else:
                    u = map_email_idx[mail]
                    v = i
                    ds.union_by_size(u, v)

        email_groups = defaultdict(list)
        for mail, idx in map_email_idx.items():
            ulp = ds.find_ulp_node(idx)
            # ulp = ds.parent[idx]
            email_groups[ulp].append(mail)

        # print(email_groups)
        res = []
        for idx, emails in email_groups.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emails))
        return res   
    
# https://www.naukri.com/code360/problems/number-of-islands-ii_1266048

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [0] * (n+1)
    
    def find_ulp_node(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.find_ulp_node(self.parent[node])
        return self.parent[node]
    
    def union_by_size(self, u, v):
        ulp_u = self.find_ulp_node(u)
        ulp_v = self.find_ulp_node(v)

        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]
        
def isValid(r, c, n, m):
    return 0 <= r < n and 0 <= c < m

def numOfIslandsII(n, m, operators):
    ds = DisjointSet(n * m)
    vis = [[0] * m for _ in range(n)]
    cnt = 0
    ans = []

    for row, col in operators:
        if vis[row][col] == 1:
            ans.append(cnt)
            continue

        vis[row][col] = 1
        cnt += 1

        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        for i in range(4):
            adjr = row + dr[i]
            adjc = col + dc[i]
            if isValid(adjr, adjc, n, m) and vis[adjr][adjc] == 1:
                nodeNo = row * m + col
                adjNodeNo = adjr * m + adjc
                if ds.find_ulp_node(nodeNo) != ds.find_ulp_node(adjNodeNo):
                    cnt -= 1
                    ds.union_by_size(nodeNo, adjNodeNo)
        ans.append(cnt)
    return ans


# https://leetcode.com/problems/making-a-large-island/description/
class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find_ulp(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find_ulp(self.parent[node])
        return self.parent[node]

    def union_by_size(self, u, v):
        ulp_u = self.find_ulp(u)
        ulp_v = self.find_ulp(v)
        if ulp_u == ulp_v:
            return
        
        if self.size[ulp_u] < self.size[ulp_v]:
            self.size[ulp_v] += self.size[ulp_u]
            self.parent[ulp_u] = ulp_v
        else:
            self.size[ulp_u] += self.size[ulp_v]
            self.parent[ulp_v] = ulp_u
   
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        nodes = n * n
        ds = DisjointSet(nodes)

        # Step 1: Union adjacent 1's
        direc = [0, 1, 0 , -1, 0]
        found_zero = False
        for i in range(n):
            for j in range(n):
                node = i * n + j
                if grid[i][j] == 1:
                    for k in range(4):
                        x = i + direc[k]
                        y = j + direc[k+1]
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            adj_node = x * n + y
                            ds.union_by_size(node, adj_node)

                elif grid[i][j] == 0:
                    found_zero = True

        if found_zero == False:
            return n*n

        # Step 2: Find largest island
        res = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    st = set()
                    curr = 0
                    for k in range(4):
                        x = i + direc[k]
                        y = j + direc[k+1]
                        if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:
                            adj_node = x * n + y
                            ulp_adj_node = ds.find_ulp(adj_node)
                            if ulp_adj_node not in st:
                                st.add(ulp_adj_node)
                                curr += ds.size[ulp_adj_node]
                    res = max(res, curr)
        return res+1


# https://leetcode.com/problems/swim-in-rising-water/submissions/1609129332/

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pq = [(grid[0][0], 0, 0)]  # (time, x, y)
        vis = [[0] * n for _ in range(n)]
        vis[0][0] = 1
        direc = [0, 1, 0, -1, 0]

        while pq:
            time, x, y = heapq.heappop(pq)

            if x == n - 1 and y == n - 1:
                return time

            for k in range(4):
                dx = x + direc[k]
                dy = y + direc[k + 1]

                if 0 <= dx < n and 0 <= dy < n and not vis[dx][dy]:
                    vis[dx][dy] = 1
                    new_time = max(time, grid[dx][dy])
                    heapq.heappush(pq, (new_time, dx, dy))
        
        return -1

