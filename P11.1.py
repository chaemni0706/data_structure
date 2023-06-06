vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
weight = [ [None,	29,		None,	None,	None,   10,		None],
           [29,	None,	16,		None,	None,	None,	15  ],
           [None,	16,		None,	12,		None,	None,	None],
           [None,	None,   12,		None,	22,		None,	18  ],
           [None,	None,	None,   22,		None,	27,		25  ],
           [10,	None,	None,	None,   27,		None,	None],
           [None,  15,		None,   18,		25,		None,	None]]    
graph = (vertex, weight)				

def weightSum( vlist, W ): #매개변수:정점 리스트, 인접 행렬		
    sum = 0 #가중치의 합
    for i in range(len(vlist)) : #모든 정점에 대해 (i: 0, ... n-1 )
        for j in range(i+1, len(vlist)): #하나의 행에 대해(삼각영역)
            if W[i][j] != None : #만약 간신이 있으면
                sum += W[i][j]	#sum에 추가
    return sum	#전체 가중치 합을 반환

print('AM : weight sum = ', weightSum(vertex, weight))

def printAllEdges(vlist, W ):	#매개변수: 정점 리스트, 인접 행렬	           
    for i in range(len(vlist)) :
        for j in range(i+1, len(W[i])) : #모든 간선 W[i][j]에 대해
            if W[i][j] != None and W[i][j] != 0 : #간섭이 있으면
                print("(%s,%s,%d)"%(vlist[i],vlist[j],W[i][j]), end=' ')
    print()

printAllEdges(vertex, weight)

graphAL ={'A' : set([('B',29),('F',10)          ]),
        'B' : set([('A',29),('C',16), ('G',15)]),
        'C' : set([('B',16),('D',12)          ]),
        'D' : set([('C',12),('E',22), ('G',18)]),
        'E' : set([('D',22),('F',27), ('G',25)]),
        'F' : set([('A',10),('E',27)          ]),
        'G' : set([('B',15),('D',18), ('E',25)]) }

def weightSum(graph):			
    sum = 0
    for v in graph:             
        for e in graph[v]:      
            sum += e[1]			
    return sum//2				

def printAllEdges(graph):
    printed_edges = set()  #중복을 제거하기 위한 집합
    for v in graph:
        for e in graph[v]:
            edge = (v, e[0], e[1])  #간선 정보를 튜플로 저장
            reversed_edge = (e[0], v, e[1])  #반대 방향의 간선 정보도 저장
            if edge not in printed_edges and reversed_edge not in printed_edges:
                #현재 간선이나 반대 방향의 간선이 이미 출력된 간선에 포함되어 있지 않으면 출력
                printed_edges.add(edge)
                print("(%s,%s,%d)" % (edge[0], edge[1], edge[2]), end=' ')

printAllEdges(graphAL)