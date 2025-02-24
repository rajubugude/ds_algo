from collections import deque

def bfs_single(adjList):
    n = len(adjList)
    queue = deque()
    vis = [0] * n
    ans = []
    bfs_helper(queue, vis, 0, ans)
    return ans

def bfs_disconnected(adjList):
    n = len(adjList)
    queue = deque()
    vis = [0] * n
    ans = []
    for i in range(n):
        if not vis[i]:
            bfs_helper(queue, vis, i, ans)
    return ans

def bfs_helper(queue, vis, node, ans):
    vis[node] = 1
    queue.append(node)
    while queue:
        currNode = queue.popleft()
        vis[currNode] = 1
        ans.append(currNode)
        for adjNode in adjList[currNode]:
            if not vis[adjNode]:
                vis[adjNode] = 1
                queue.append(adjNode)
    return ans




def createAdjList(n, edgeList):
    adjList = [[] for _ in range(n)]
    for u, v in edgeList:
        adjList[u].append(v)
        adjList[v].append(u)
    return adjList

edgeList = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4),
             (3, 4), (5, 6), (5, 7), (7, 8)]
n = 9 # numer od nodes, for creating adjlist
adjList = createAdjList(n, edgeList)

print("given adjlist", adjList)
print("prints only connected comp", bfs_single(adjList))
print("prints all components", bfs_disconnected(adjList))


#     0 
# 1------ 2      5----7
# |        |     |    |
# 3------ 4      6    8