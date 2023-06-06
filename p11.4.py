INF = 9999 #가장 큰 가중치(무한대)

def getMinVertex(dist, selected): #현재 트리에 인접한 정점들 중에서 가장 가까운 정점을 찾는 함수
    minv = 0
    mindist = INF
    for v in range(len(dist)): #모든 정점들에 대해
        if not selected[v] and dist[v] < mindist: #선택 안 되었고
            mindist = dist[v] #가중치가 작으면
            minv = v #minv 갱신
    return minv #최소 가중치의 정점 반환

def MSTPrim(vertex, adj): #Prim의 최소 비용 신장 트리 프로그램
    vsize = len(vertex)
    dist = [INF] * vsize #dist: [INF, INF, ..., INF]
    selected = [False] * vsize #selected: [False, False,..., False]
    dist[0] = 0 #dist: [0, INF, ..., INF]
    totalWeight = 0  # MST의 가중치 합을 누적할 변수

    for i in range(vsize): #정점의 수 만큼 반복
        u = getMinVertex(dist, selected)
        selected[u] = True #u는 이제 선택됨
        print(vertex[u], end=' ') #u를 출력

        for v in range(vsize): #내부 루프
            if adj[u][v] is not None: #(u,v) 간선이 있으면 dust[v] 갱신
                if selected[v] is False and adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]
        totalWeight += dist[u]  # 선택된 간선의 가중치를 누적

    print()
    print("MST의 가중치 합:", totalWeight)


vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None, 29, None, None, None, 10, None],
          [29, None, 16, None, None, None, 15],
          [None, 16, None, 12, None, None, None],
          [None, None, 12, None, 22, None, 18],
          [None, None, None, 22, None, 27, 25],
          [10, None, None, None, 27, None, None],
          [None, 15, None, 18, 25, None, None]]

print("MST By Prim's Algorithm")
MSTPrim(vertex, weight)