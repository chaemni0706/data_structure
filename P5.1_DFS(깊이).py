#깊이 우선 탐색
from queue import Queue

def isValidPos(x, y): #현재위치 (x,y)가 미로 안에 있고, 벽이 아니면 True를 반환함
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def DFS(): #깊이우선탐색
    que = Queue()
    que.put((0, 1))
    print('DFS: ', end='') #출력을 DFS로 변경

    while not que.empty():
        here = que.get()
        print(here, end='->')
        x, y = here
        if map[y][x] == 'x': #x를 찾으면 True 반환
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y - 1): #상
                que.put((x, y - 1))
            if isValidPos(x, y + 1):#하
                que.put((x, y + 1))
            if isValidPos(x - 1, y): #좌
                que.put((x - 1, y))
            if isValidPos(x + 1, y): #우
                que.put((x + 1, y))
    return False #이동할 수 없으면 False 반환

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
] #1=벽, 0=이동가능공간, e=출발지점, x=목적지
MAZE_SIZE = 6 #미로 크기

result = DFS()
if result:
    print('미로탐색 성공')
else:
    print('미로탐색 실패')