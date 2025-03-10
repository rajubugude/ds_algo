from typing import List
from collections import deque

directions = [0, 1, 0, -1, 0]
# https://leetcode.com/problems/number-of-provinces/
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        count = 0
        vis = [0]*n 
        for i in range(n):
            if not vis[i]:
                # self.dfs(vis, i, isConnected, n)
                self.bfs(vis, i, isConnected, n)
                count += 1
        return count
    
    def bfs(self,vis,node,grid,n):
        queue = deque()
        queue.append(node)
        vis[node] = 1
        while queue:
            curr_node = queue.popleft()
            for adjNode in range(n):
                if not vis[adjNode] and grid[curr_node][adjNode] == 1:
                    vis[adjNode] = 1
                    queue.append(adjNode)


    def dfs(self,vis,node,grid,n):
        vis[node] = 1
        for adjNode in range(n):
            if not vis[adjNode] and grid[node][adjNode] == 1:
                vis[adjNode] = 1
                self.dfs(vis, adjNode, grid, n)


# https://leetcode.com/problems/flood-fill/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        org_color = image[sr][sc]
        if org_color == color:
            return image
        self.bfs(sr, sc, org_color, color, image, m, n)
        # self.dfs(sr, sc, org_color, color, image, m, n)
        return image
    
    def bfs(self, sr, sc, org_color, new_color, image, m, n):
        queue = deque()
        queue.append((sr,sc))
        image[sr][sc] = new_color
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                dx = x + directions[k]
                dy = y + directions[k+1]
                if 0 <= dx < m and 0 <= dy < n and image[dx][dy] == org_color:
                    image[dx][dy] = new_color
                    queue.append((dx,dy))
        

    def dfs(self, x, y, org_color, color, image, m, n):
        if x >= m or x < 0 or y >= n or y < 0 or image[x][y] != org_color or\
           image[x][y] == color:
            return  
        image[x][y] = color
        for k in range(4):
            dx = x + directions[k]
            dy = y + directions[k+1]
            self.dfs(dx, dy, org_color, color, image, m, n)


directions = [0, 1, 0, -1, 0]
# https://leetcode.com/problems/surrounded-regions/-
class Solution:
    def dfs(self, i, j, board, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
            return
        board[i][j] = 'A' #any random char, just to identify
        for k in range(4):
            dx = i + directions[k]
            dy = j + directions[k+1]
            self.dfs(dx, dy, board, m, n)

    def bfs(self, queue, board, m, n):
        while queue:
            x,y = queue.popleft()
            board[x][y] = 'A'
            for k in range(4):
                dx = x + directions[k]
                dy = y + directions[k+1]
                if 0 <= dx < m and 0 <= dy < n and board[dx][dy] == 'O':
                    board[dx][dy] = 'A'
                    queue.append((dx,dy))


    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        queue = deque()
        # on the borders apply bfs/dfs if it is 'O'
        for i in range(m):
            if board[i][0] == 'O':
                # self.dfs(i, 0, board, m, n)
                queue.append((i,0))
            if board[i][n-1] == 'O':
                # self.dfs(i, n-1, board, m, n)
                queue.append((i,n-1))

        for i in range(n):
            if board[0][i] == 'O':
                # self.dfs(0, i, board, m, n)
                queue.append((0,i))
            if board[m-1][i] == 'O':
                # self.dfs(m-1, i, board, m, n)
                queue.append((m-1,i))
                
        self.bfs(queue, board, m, n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'
        return board


# https://leetcode.com/problems/number-of-enclaves/
directions = [0, 1, 0, -1, 0]
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count_ones = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    if grid[i][j] == 1:
                        # self.bfs(grid, i, j, m, n)
                        self.dfs(grid, i, j, m, n)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count_ones += 1
        return count_ones
    
    def dfs(self, grid, i, j, m, n):
        if i < 0 or  i>= m or j < 0 or j >= n or grid[i][j] == 0:
            return
        grid[i][j] = 0
        for k in range(4):
            dx = i + directions[k]
            dy = j + directions[k+1]
            self.dfs(grid, dx, dy, m, n)

    def bfs(self, grid, i, j, m, n):
        queue = deque()
        queue.append((i,j))
        grid[i][j] = 0
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                dx = x + directions[k]
                dy = y + directions[k+1]
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                    grid[dx][dy] = 0
                    queue.append((dx,dy)) 


# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, n: int, adj) -> bool:
        vis = [0] * n  # Visited array

        for node in range(n):  # Check all components (for disconnected graphs)
            if not vis[node]:  
                # Uncomment one of the methods (DFS or BFS)
                # if self.bfs(node, vis, adj):  
                if self.dfs(node, -1, vis, adj):  
                    return True  
        return False  

    # DFS approach to detect a cycle
    def dfs(self, node: int, parent: int, vis: List[int], adj: List[List[int]]) -> bool:
        vis[node] = 1  # Mark the current node as visited

        for adj_node in adj[node]:  
            if not vis[adj_node]:  # If adjacent node is not visited, recurse
                if self.dfs(adj_node, node, vis, adj):
                    return True  
            elif adj_node != parent:  # If visited and not parent, cycle exists
                return True  

        return False  

    # BFS approach to detect a cycle
    def bfs(self, node: int, vis: List[int], adj: List[List[int]]) -> bool:
        queue = deque([(node, -1)])  # (current_node, parent)
        vis[node] = 1  # Mark as visited before adding to queue

        while queue:
            curr_node, parent = queue.popleft()

            for adj_node in adj[curr_node]:
                if not vis[adj_node]:  
                    vis[adj_node] = 1  # Mark as visited before enqueueing
                    queue.append((adj_node, curr_node))
                elif adj_node != parent:  # If visited and not parent, cycle exists
                    return True  

        return False  



# https://www.geeksforgeeks.org/problems/number-of-distinct-islands/0
import sys
from typing import List
sys.setrecursionlimit(10**8)
directions = [0, 1, 0, -1, 0]
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        # code here
        path_set = set()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    shape = []
                    # self.dfs(i, j, i, j, shape, n, m, grid)
                    self.bfs(i, j, i, j, shape, n, m, grid)
                    path_set.add(tuple(shape))
        return len(path_set)
    
    def bfs(self, x, y, base_x, base_y, shape, n, m, grid):
        queue = deque()
        queue.append((x,y))
        curr_path = (base_x-x, base_y-y)
        shape.append(curr_path)
        grid[x][y] = 0
        while queue:
            u, v = queue.popleft()
            for k in range(4):
                dx = u + directions[k]
                dy = v + directions[k+1]
                if 0 <= dx < n and 0 <= dy < m and grid[dx][dy] == 1:
                    queue.append((dx,dy))
                    curr_path = (base_x-dx, base_y-dy)
                    shape.append(curr_path)
                    grid[dx][dy] = 0
            
    
    def dfs(self, x, y, base_x, base_y, shape, n, m, grid):
        if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
            return
        
        grid[x][y] = 0
        curr_path = (base_x-x, base_y-y)
        shape.append(curr_path)
        for k in range(4):
            dx = x + directions[k]
            dy = y + directions[k+1]
            self.dfs(dx, dy, base_x, base_y, shape, n, m, grid)


# https://leetcode.com/problems/is-graph-bipartite/            
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n

        for node in range(n):
            if color[node] == -1:
                # if not self.bfs(node, color, graph):
                #     return False
                color[node] = 0 
                if not self.dfs(node, color, graph):
                    return False
        return True

    def dfs(self, node, color, graph):
        for adj_node in graph[node]:
            if color[adj_node] == -1:
                color[adj_node] = 1 - color[node]
                if not self.dfs(adj_node, color, graph):
                    return False
            elif color[adj_node] == color[node]:
                return False
        return True

    def bfs(self, node, color, graph):
        queue = deque([node])
        color[node] = 0
        while queue:
            curr = queue.popleft()
            for adj in graph[curr]:
                if color[adj] == -1:
                    color[adj] = 1 - color[curr]
                    queue.append(adj)
                elif color[adj] == color[curr]:
                    return False
        return True


#TODO: get max_sum of all the possible paths through dfs
# https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
class Solution:
    def fill_bob_path(self, node, graph, vis):
        if node == 0:
            return [0]  # Found root

        vis[node] = 1
        for adjNode in graph[node]:
            if not vis[adjNode]:
                result = self.fill_bob_path(adjNode, graph, vis)
                if result:
                    return [node] + result  # Build path by appending `node`
        
        return [] 

    def max_profit_path(self, bob_time, node, parent, time, graph, amount, curr_sum):        
        if time < bob_time[node] or bob_time[node] == -1:
            curr_sum += amount[node]

        elif time == bob_time[node]:
            curr_sum += (amount[node]//2)

        #base case - leafnode
        if len(graph[node]) == 1 and node != 0:
            return curr_sum
        maxi = float('-inf')
        for adjNode in graph[node]:
            if adjNode != parent:
                maxi = max(maxi, self.max_profit_path(bob_time, 
                        adjNode, node, time+1, graph, amount, curr_sum))
        
        return maxi

    def mostProfitablePath(self, edges, bob, amount):
        n = len(amount)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        n = len(amount)
        vis = [0] * n
        path = self.fill_bob_path(bob, graph, vis)
        bob_time = [-1] * n
        for i in range(len(path)):
            bob_time[path[i]] = i
        return self.max_profit_path(bob_time, 0, -1, 0, graph, amount, 0)


# https://leetcode.com/problems/map-of-highest-peak/
# https://leetcode.com/problems/01-matrix/description/class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        heights = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    heights[i][j] = 0
        directions = [0, 1, 0, -1, 0]
        while queue:
            x, y  = queue.popleft()
            for k in range(4):
                dx = x + directions[k]
                dy = y + directions[k+1]
                if 0 <= dx < m and 0 <= dy < n and heights[dx][dy] == -1:
                    queue.append((dx, dy))
                    heights[dx][dy] = 1 + heights[x][y]
        return heights
        

# https://leetcode.com/problems/word-ladder/description/
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordsSet = set(wordList)
        if endWord not in wordsSet:
            return 0

        queue = deque()
        queue.append((beginWord,1))
        while queue:
            word,ans = queue.popleft()
            if word == endWord:
                return ans
            for i in range(len(word)):
                temp_word = ''
                for j in range(26):
                    new_char = chr(ord('a') + j)
                    temp_word = word[:i] + new_char + word[i+1:]
                    if temp_word in wordsSet:
                        wordsSet.remove(temp_word)
                        queue.append((temp_word,ans+1))
        return 0


# https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1
class Solution:
    def isCyclic(self, adj : List[List[int]]) -> bool :
        n = len(adj)
        vis = [0]*n
        dfs_vis = [0]*n
        for node in range(n):
            if not vis[node]:
                if self.dfs(vis, dfs_vis, adj, node):
                    return True
        return False
    
    def dfs(self, vis, dfs_vis, adj, node):
        vis[node] = 1
        dfs_vis[node] = 1
        for adj_node in adj[node]:
            if not vis[adj_node]:
                if self.dfs(vis, dfs_vis, adj, adj_node):
                    return True
            elif dfs_vis[adj_node] == 1:
                return True
        dfs_vis[node] = 0 
        return False


# https://leetcode.com/problems/find-eventual-safe-states/description/
class Solution:
    def eventualSafeNodes(self, adj: List[List[int]]) -> List[int]:
        n = len(adj)
        vis = [0] * n
        dfs_vis = [0]*n
        ans = set()
        for node in range(n):
            if not vis[node]:
                self.dfs(node, vis, dfs_vis, adj, ans)
        
        safe_nodes = []
        for i in range(n):
            if i in ans:
                safe_nodes.append(i)
        return safe_nodes
        
    
    def dfs(self, node, vis, dfs_vis, adj, ans):
        vis[node] = 1
        dfs_vis[node] = 1
        for adj_node in adj[node]:
            if dfs_vis[adj_node]:
                return True
            if not vis[adj_node]:
                if self.dfs(adj_node, vis, dfs_vis, adj, ans):
                    return True
        
        ans.add(node)
        dfs_vis[node] = 0
        return False
