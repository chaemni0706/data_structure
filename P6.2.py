class Node: #단순 연결 리스트를 위한 노드 클래스
    def __init__(self, elem, link=None): #생성자, 디폴트 인수 사용
        self.data = elem #데이터 멤버 생성 및 초기화
        self.link = link #링크 생성 및 초기화

class LinkedStack: #연결 스택 클래스
    def __init__(self):  #생성자
        self.top = None #top 생성 및 초기화
    def isEmpty(self): #공백상태 검사
        return self.top == None
    def clear(self): #스택 초기화
        self.top = None
    def push(self, item): #연결 스택의 삽입 연산
        n = Node(item, self.top) #입력 데이터를 이용해 새로운 노드 n을 생성+n의 링크가 시작 노드를 가리키도록 함
        self.top = n #top이 n을 가리키도록 함
    def pop(self): #연결된 스택의 삭제 연산
        if not self.isEmpty(): #공백이 아니면
            n = self.top #변수 n이 시작 노드를 가리키도록 함
            self.top = n.link #top이 다음 노드를 가리키도록 함
            return n.data #n이 가리키는 노드의 데이터를 반환
        else: #공백이면
            return None #none 반환
    def size(self): #스택의 항목 수 계산
        self.top=None
    def display(self, msg): #스택의 항목 출력 함수
        self.head=None #리스트의 초기화

    def getNode(self, pos): #pos번째 노드 반환
        if pos<0:
            return None 
        node=self.head; #node를 다음 노드로 이동
        while pos>0 and node != None: #pos번 반복
            node = node.link #node를 다음 노드로 이동
            pos-=1 #남은 반복 횟수 줄임
        return node #최종 노드 반환
    
    def getEntry(self, pos): #pos 번째 노드와 데이터 반환
        node=self.getNode(pos) #pos번째 노드
        if node == None:#찾는 노드가 없는 경우
            return None #그 노드의 데이터 필드 반환
        else:
            return node.data #그 노드의 데이터 필드 반환
        
    def replace(self,pos,elem): #pos번째 노드의 데이터를 변경
        node=self.getNode(pos) #pos번째 노드를 찾아
        if node!=None: #데이터 필드에 elem 복사
            node.data=elem
    
    def find(self, data): #데이터로 data를 갖는 노드 반환
        node=self.head; 
        while node is not None: #모든 노드에서 찾음
            if node.data==data: #찾아지면 바로 반환
                return node 
            node=node.link 
        return None #찾아지지 않으면 none 반환
    
    def insert(self, pos, elem): 
        before=self.getNode(pos-1) #before 노드를 찾음
        if before==None: #맨 앞에 삽입하는 경우
            self.head=Node(elem, self.head) #맨 앞에 삽입함
        else: #중간의 앞에 삽입하는 경우
            node=Node(elem, before.link) #노드 생성
            before.link=node

    def delete(self, pos): 
        before=self.getNode(pos-1) #before 노드를 찾음
        if before==None: #시작 노드를 삭제
            if self.head is not None: #공백이 아니면
                self.head=self.head.link #head를 다음으로 이동
        elif before.link!=None: #중간에 있는 노드 삭제
            before.link=before.link.link
    
    def merge(self, other): #self, other 연결 리스트를 병합
        node = self.top
        if node == None: #self.top이 None이면 other.top을 self.top으로 설정
            self.top = other.top
        else: #그렇지 않으면
            while node.link != None: #node의 다음 노드가 None이 될때까지 이동
                node = node.link 
            node.link = other.top #node링크에 oter.top을 할당
        other.clear() #other를 초기화

class LinkedList: #LinkedList 클래스
    def __init__(self): #생성자
        self.head = None 
        self.tail = None

    def isEmpty(self): #공백상태 검사
        return self.head is None

    def append(self, elem): #새로운 노드를 연결 리스트의 마지막에 추가하는 함수
        node = Node(elem)
        if self.head is None: #head가 None인 경우 head를 새로운 노드로 설정
            self.head = node
        else: #그렇지 않으면
            self.tail.link = node #마지막 노드의 link를 새로운 노드로 설정
        self.tail = node #tail을 새로운 노드로 설정

    def merge(self, other):  #self 리스트와 other 리스트를 병합
        if other.head is None: #other 리스트가 비어 있으면 암것도 안 함
            return

        if self.head is None: #self 리스트가 비어있는 경우
            self.head = other.head #other 리스트를 그대로 복사
            self.tail = other.tail #self리스트의 마지막 노드와 other 리스트의 첫번째 노드를 연결
            return

        self.tail.link = other.head #self리스트의 tail을 other 리스트의 heead와 tail을 None으로
        self.tail = other.tail
        other.head = None
        other.tail = None

A = LinkedList() #A리스트에 1, 2, 3 추가
A.append(1)
A.append(2)
A.append(3)

B = LinkedList() #B리스트에 4, 5, 6 추가
B.append(4)
B.append(5)
B.append(6)

A.merge(B) #A와 B리스트 병합

print("A:") #1 2 3 4 5 6 출력됨
node = A.head
while node is not None:
    print(node.data, end=" ")
    node = node.link #A 출력
print( '/n')
print("B:") #B리스트는 A리스트와 병합 했기 때문에 None
node = B.head
while node is not None:
    print(node.data, end=" ")
    node = node.link #B 출력