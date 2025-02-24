# degrees = no. of neighbour nodes
# num of degress = 2 * Edges
# TC = O(numOfNode + 2(Edges))
# SC = O(3N) ~ O(N)



u, v = (map(int, input().split()))
l = [u, v]
print(l)
print(type(l))

# input() takes user input as a string.
# .split() breaks the input into separate string values.
# map(int, ...) converts those split values into integers.
# u, v = ... unpacks the two integer values into u and v.

# edgeList = []
# n = int(input("Enter the number of nodes: "))
# m = int(input("Enter the number of edges: "))
# for _ in range(m):
#     u, v = map(int, input().split())
#     edgeList.append((u, v))

# print(edgeList)

edgeList = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 4),
             (3, 4), (5, 6), (5, 7), (7, 8)]

def createAdjList(n, edgeList):
    adjList = [[] for _ in range(n)]
    for u, v in edgeList:
        adjList[u].append(v)
        adjList[v].append(u)
    return adjList

n = 9 # numer od nodes, for creating adjlist
adjList = createAdjList(n, edgeList)