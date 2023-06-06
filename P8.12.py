class TNode: #이진트리를 위한 노드 클래스
    def __init__ (self, data, left, right): #생성자
        self.data=data #노드의 데이터
        self.left=left #왼쪽 자식을 위한 링크
        self.right=right #오른쪽 자식을 위한 링크

MAX_QSIZE=10

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def enqueue(self, item):
        node = TNode(item, None, None)
        if self.isEmpty():
            node.left = node
            self.tail = node
        else:
            node.left = self.tail.left
            self.tail.left = node
        self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % MAX_QSIZE
            return data
    
    def isEmpty(self):
        return self.front == self.rear

def preorder(n): #전위 순회 함수
    if n is not None:
        print(n.data, end=" ") #먼저 루트 노드 처리(화면 출력)
        preorder(n.left) #왼쪽 서브트리 처리
        preorder(n.right) #오른쪽 서브트리 처리

def inorder(n): #중위 순회 함수
    if n is not None: 
        inorder(n.left) #왼쪽 서브 트리 처리
        print(n.data, end=' ') #루트 노드 처리(화면 출력)
        inorder(n.right) #오른쪽 서브트리 처리

def postorder(n): #후위 순회 함수
    if n is not None:
        postorder(n.left) #왼쪽 서브트리 처리
        postorder(n.right) #오른쪽 서브트리 처리
        print(n.data, end=' ')

def levelorder(root):
    queue=CircularQueue() #큐 객체 초기화
    queue.enqueue(root) #최초에 큐에는 루트 노드만 들어 있음
    while not queue.isEmpty(): #큐가 공백 상태가 아닌 동안
        n=queue.dequeue() #큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data, end=' ') #먼저 노드의 정보를 출력
            queue.enqueue(n.left) #n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right) #n의 오른쪽 자식 노드를 큐에 삽입

def count_node(n): #순환을 이용해 트리의  노드 수를 계산하는 함수
    if n is None: #n이 None이면 공백 트리 -> 0을 반환
        return 0
    else: #좌우 서브 트리의 노드 수의 합+1을 반환(순환 이용)
        return 1+count_node(n.left)+count_node(n.right)
    
def count_leaf(n): 
    if n is None: #공백 트리 -> 0을 반환
        return 0
    elif n.left is None and n.right is None: #단말 노드 -> 1을 반환
        return 1
    else: #비단말 노드: 좌우 서브 트리의 결과 합을 반환
        return count_leaf(n.left)+count_leaf(n.right)
    
def calc_height(n): 
    if n is None: #공백 트리 -> 0을 반환
        return 0
    hLeft=calc_height(n.left) #왼쪽 트리의 높이 -> hLeft
    hRight=calc_height(n.right) #오른쪽 트리의 높이 -> hRight
    if (hLeft>hRight): #더 높은 높이에 1을 더해 반환
        return hLeft+1
    else:
        return hRight+1

a=TNode('A', None, None)
b=TNode('B', None, None)
divide=TNode('/', a, b)
c=TNode('C', None, None)
multiply1=TNode('*', divide, c)
d=TNode('D', None, None)
multiply2=TNode('*', multiply1, d)
e=TNode('E', None, None)
root=TNode('A', multiply2, e)

print('\n In-Order: ', end='')
inorder(root)
print('\n Pre-Order: ', end='')
preorder(root)
print('\n Post-Order: ', end='')
postorder(root)
print('\n Level-Order: ', end='')
levelorder(root)
print()

print("노드의 개수=%d개" %count_node(root))
print("단말의 개수=%d개" %count_leaf(root))
print("트리의 높이=%d"%calc_height(root))