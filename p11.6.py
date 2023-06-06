INF = 9999 #가장 큰 가중치

def choose_vertex(dist, found): #최소 거리와 그 위치를 찾음
    min_dist = INF
    min_pos = -1
    for i in range(len(dist)):
        if dist[i] < min_dist and not found[i]:
            min_dist = dist[i]
            min_pos = i
    return min_pos

def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)
    dist = list(adj[start])
    path = [start] * vsize
    found = [False] * vsize
    found[start] = True
    dist[start] = 0

    for i in range(vsize): #최소 거리를 가진 정점을 선택
        print("Step %2d: " % (i + 1), dist)
        u = choose_vertex(dist, found)
        found[u] = True

        for w in range(vsize):
            if not found[w]: #선택된 정점을 통해 갈 수 있는 더 짧은 거리를 찾음
                if dist[u] + adj[u][w] < dist[w]:
                    dist[w] = dist[u] + adj[u][w]
                    path[w] = u

    return path, dist

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[0, 7, INF, INF, 3, 10, INF],
          [7, 0, 4, 10, 2, 6, INF],
          [INF, 4, 0, 2, INF, INF, INF],
          [INF, 10, 2, 0, 11, 9, 4],
          [3, 2, INF, 11, 0, 13, 5],
          [10, 6, INF, 9, 13, 0, INF],
          [INF, INF, INF, 4, 5, INF, 0]]

print("Shortest Path By Dijkstra Algorithm")
start = 0
path, dist = shortest_path_dijkstra(vertex, weight, start)

print("Src->Dst  Dist  Path")
for end in range(len(vertex)):
    if end != start:
        print("%s->%s\t%3d\t%s" % (vertex[start], vertex[end], dist[end], vertex[start]), end='')
        while path[end] != start:
            print(" %s" % vertex[path[end]], end='')
            end = path[end]
        print(" %s" % vertex[path[end]])