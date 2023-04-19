class Queue:
    def __init__(self): #스택을 빈 리스트로 초기화
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self, val): #입력이 들어오면 스택1에 넣음
        self.stack1.append(val)
    
    def dequeue(self): #출력 요청이 들어오면 스택2에서 요소를 꺼내고 스택2가 비어있을 때는 스택 1의 모든 요소를 꺼내서 스택 2에넣음
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

q = Queue() #입력 순서대로 저장함
q.enqueue(1) #스택 1에 1, 2, 3 저장
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  #스택 2에서 꺼내옴
print(q.dequeue()) 
q.enqueue(4) #
print(q.dequeue())  #3
print(q.dequeue())  #4
print(q.dequeue())  #None