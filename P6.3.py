class Queue: #queue 클래스 선언
    class Node: #node 클래스 선언
        def __init__(self, data): #생성자
            self.data = data 
            self.next = None
    
    def __init__(self):
        self.front = None #front는 전단
        self.rear = None #rear은 후단
    
    def isEmpty(self): #큐가 비었는지 검사
        return self.front is None #front가 None이면 비었다고 판단
    
    def enqueue(self, data): #큐에 데이터를 추가
        new_node = Queue.Node(data) #새로운 노드를 생성하고 노드의 데이터를 인자로 받아 초기화 함
        if self.is_empty(): #비었다면
            self.front = new_node #새로운 노드를 front로
        else: #안 비었다
            self.rear.next = new_node #self.rear의다음 노드로 새로운 노드를 ㅈ정
        self.rear = new_node #rear을 새로운 노드로 지정
    
    def dequeue(self): #큐에서 데이터 삭제하고 반환함
        if self.is_empty(): #비었다면
            return #return 
        data = self.front.data #front의 데이터를 data에 저장
        self.front = self.front.next #front를 front의 다음 노드로 지정
        if self.front is None: #front가 None이라면, 
            self.rear = None #rear도 None
        return data #data 반환

MAX_QSIZE=10 #원형 큐의 크기

class CircularQueue:
    def __init__(self): #CircularQueue 생성자
        self.front=0 #큐의 전단 위치 
        self.rear=0 #큐의 후단 위치
        self.items=[None]*MAX_QSIZE #항목 저장용 리스트
    def isEmpty(self): #공백 검사
        return self.front == self.rear
    def isFull(self):
        return self.front==(self.rear+1)%MAX_QSIZE
    def clear(self):
        self.front=self.rear
    def enqueue(self,item): 
        if not self.isFull(): #포화상태가 아니면
            self.rear=(self.rear+1)%MAX_QSIZE #rear회전
            self.items[self.rear]=item #rear 위치에 삽입
    def dequeue(self):
        if not self.isEmpty(): #공백상태가 아니면
            self.front=(self.front+1)%MAX_QSIZE #front 회전
            return self.items[self.front] #front 위치의 항목 반환
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear-self.front+MAX_QSIZE)%MAX_QSIZE
    
    def display(self):
        out=[]
        if self.front<self.rear:
            out=self.items[self.front+1:self.rear+1]
        else:
            out=self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%s, r=%d]=>" %(self.front, self.rear), out)

q=CircularQueue() #원형큐 만들기 
for i in range(8): #0~7 삽입
    q.enqueue(i) 
q.display() #원형 큐에서 구현한 print() 호출
for i in range(5): #5번 삭제
    q.dequeue(); 
q.display()
for i in range(8, 14): #8~13 삽입
    q.enqueue(i)
q.display()
