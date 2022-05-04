import sys

INF = sys.maxsize
def floydWarshall(graph,n): #n=no. of vertex
    dist=graph
    for k in range(n):
        for i in range(n):
            for j in range(n): 
                dist[i][j] = min(dist[i][j] ,dist[i][k]+ dist[k][j])
    return dist

graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0,   1],
         [INF, INF, INF, 0]
        ]
n =4

print(floydWarshall(graph, n))