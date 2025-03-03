def dfs_helper(ans, vis, node, adjList):
    vis[node] = 1
    ans.append(node)
    for adjNode in adjList[node]:
        if not vis[adjNode]:
            dfs_helper(ans, vis, adjNode, adjList)


def dfs_single(adjList):
    n = len(adjList)
    vis = [0] * n
    ans = []
    dfs_helper(ans, vis, 0, adjList)
    return ans

def dfs_disconnected(adjList):
    n = len(adjList)
    vis = [0] * n
    ans = []
    for i in range(n):
        if not vis[i]:
            dfs_helper(ans, vis, i, adjList)
    return ans

n = 9 # numer od nodes, for creating adjlist

def createAdjList(n, edgeList):
    adjList = [[] for _ in range(n)]
    for u, v in edgeList:
        adjList[u].append(v)
        adjList[v].append(u)
    return adjList

edgeList = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4),
             (3, 4), (5, 6), (5, 7), (7, 8)]

#     0 
# 1------ 2      5----7
# |        |     |    |
# 3------ 4      6    8

#V - no of vertices, E - no of edges
# TC: O(V + E)
# Each node is visited once → O(V)
# Each edge is processed once in an adjacency list → O(E)
# Total: O(V + E)
# SC : O(V) (for DFS)
# Recursive DFS uses O(V) stack space in the worst case (for a completely connected graph).
adjList = createAdjList(n, edgeList)
print("given adjlist", adjList)

print("prints only connected comp", dfs_single(adjList))
print("prints all components", dfs_disconnected(adjList))
