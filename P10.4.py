def construct_spanning_tree(vertex, adjMat): #그래프 생성   
    graph = {}
    for i in range(len(vertex)):
        neighbors = set()
        for j in range(len(adjMat[i])):
            if adjMat[i][j] == 1:
                neighbors.add(j)
        graph[i] = neighbors

    visited = set() #초기화
    spanning_tree = []
 
    def dfs(start): #깊이 우선 탐색 함수
        nonlocal visited
        if start not in visited:
            visited.add(start)
            for neighbor in graph[start]:
                spanning_tree.append((vertex[start], vertex[neighbor]))  #간선 추가
                dfs(neighbor)
   
    for i in range(len(vertex)): #모든 정점에 대해 깊이 우선 탐색 수행
        dfs(i)
  
    for edge in spanning_tree: #신장 트리 출력
        print(f"{edge[0]}-{edge[1]}")

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

construct_spanning_tree(vertex, adjMat)