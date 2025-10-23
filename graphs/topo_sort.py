'''
Topological sorting only exists in Directed Acyclic Graph (DAG). 
If the nodes of a graph are connected through directed edges and the graph does 
    not contain a cycle, it is called a directed acyclic graph(DAG). 

The topological sorting of a directed acyclic graph is nothing but the linear ordering
 of vertices such that if there is an edge between node u and v(u -> v), 
 node u appears before v in that ordering.
'''

from typing import List, Dict, Set
from collections import deque, defaultdict
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
    

# https://leetcode.com/problems/find-eventual-safe-states/description/
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        indegree = [0] * n
        adj = [[] for _ in range(n)]

        for i in range(n):
            for node in graph[i]:
                adj[node].append(i)
                indegree[i] += 1

        q = deque()
        # Push all the nodes with indegree zero in the queue.
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        safe = [False] * n
        while q:
            node = q.popleft()
            safe[node] = True

            for neighbor in adj[node]:
                # Delete the edge "node -> neighbor".
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        safeNodes = []
        for i in range(n):
            if safe[i]:
                safeNodes.append(i)

        return safeNodes


# https://neetcode.io/problems/foreign-dictionary
#BFS
class Solution:
    def compare(self, word1: str, word2: str, adj: List[List[int]]) -> bool:
        """Compares two words and builds adjacency list."""
        min_length = min(len(word1), len(word2))

        for i in range(min_length):
            if word1[i] != word2[i]:  
                u = ord(word1[i]) - ord('a')
                v = ord(word2[i]) - ord('a')
                adj[u].append(v)  # Directed edge u → v
                return True  # Stop at first difference

        # Check invalid order: 'abc' before 'ab' (prefix case)
        return len(word1) <= len(word2)

    def make_adj_list(self, words: List[str]) -> tuple:
        """Builds adjacency list using a fixed-size array and tracks used characters."""
        adj = [[] for _ in range(26)]
        present = [0] * 26  

        # Mark characters present in words
        for word in words:
            for char in word:
                present[ord(char) - ord('a')] = 1

        # Build adjacency list
        for i in range(len(words) - 1):
            if not self.compare(words[i], words[i + 1], adj):
                return [], []  # Invalid ordering
        
        return adj, present

    def topoSort(self, adj: List[List[int]], present: List[int]) -> List[int]:
        indegree = [0] * 26

        # Compute indegree for each node
        for u in range(26):
            for v in adj[u]:
                indegree[v] += 1

        # Initialize queue with zero-indegree nodes
        q = deque([i for i in range(26) if present[i] and indegree[i] == 0])

        topo = []
        while q:
            node = q.popleft()
            topo.append(node)

            for v in adj[node]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        # Check for cycles
        return topo if len(topo) == sum(present) else []

    def foreignDictionary(self, words: List[str]) -> str:
        """Returns the character order in an alien dictionary."""
        adj, present = self.make_adj_list(words)
        if not adj:
            return ""

        topo = self.topoSort(adj, present)
        if not topo:
            return ""

        return "".join(chr(i + ord('a')) for i in topo)

#DFS 
class Solution:
    def build_graph(self, words: List[str]) -> Dict[str, Set[str]]:
        """Builds adjacency list for character precedence relationships."""
        # adj = {c: set() for w in words for c in w}
        adj = {}
        for word in words:
            for char in word:
                if char not in adj:
                    adj[char] = set()
        
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            
            # Invalid case: w1 is longer but starts with w2
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return {}
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break  # Only consider the first different character
        
        return adj
    
    def dfs(self, char: str, adj: Dict[str, Set[str]], visited: Dict[str, bool], res: List[str]) -> bool:
        """Performs DFS for topological sorting and cycle detection."""
        if char in visited:
            return visited[char]
        
        visited[char] = True
        
        for neighbor in adj[char]:
            if self.dfs(neighbor, adj, visited, res):
                return True
        
        visited[char] = False
        res.append(char)
        return False
    
    def topological_sort(self, adj: Dict[str, Set[str]]) -> str:
        """Executes DFS-based topological sorting and cycle detection."""
        visited = {}
        res = []
        
        for char in adj:
            if self.dfs(char, adj, visited, res):
                return ""
        
        res.reverse()
        return "".join(res)
    
    def foreignDictionary(self, words: List[str]) -> str:
        """Returns the character order in an alien dictionary."""
        adj = self.build_graph(words)
        if not adj:
            return ""
        
        return self.topological_sort(adj)

# s = Solution()
# words = ["hrn","hrf","er","enn","rfnn"]
# print(s.foreignDictionary(words))



# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/ (Revise)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {}
        graph = defaultdict(list)
        
        for i, recipe in enumerate(recipes):
            indegree[recipe] = len(ingredients[i])
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)

        # print(graph, 'gr')
        # print(indegree, 'ingre')

        queue = deque(supplies)
        result = []
        while queue:
            ingredient = queue.popleft()
            for recipe in graph[ingredient]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
        
        return result

s = Solution()
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]
print(s.findAllRecipes(recipes, ingredients, supplies))


import heapq

class Solution123:
    def dijkstra(self, n, edges, src):
        pq = []
        adj = [[] for _ in range(n)]
        # print(adj)

        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        # print(adj)

        dist = [float('inf')]*n
        dist[src] = 0
        heapq.heappush(pq, (0, src))

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > dist[curr_node]:
                continue

            for adj_node, adj_wt in adj[curr_node]:
                new_dist = curr_dist + dist[curr_node]
                if dist[adj_node] > new_dist:
                    dist[adj_node] = new_dist
                    heapq.heappush(pq, (new_dist, adj_node))

        return [-1 if x == float('inf') else x for x in dist]

s = Solution123()
V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2
print(s.dijkstra())