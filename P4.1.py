class Stack:
    def __init__(self): #생성자
        self.top=[] #top이 이제 클래스의 멤버 변수가 됨

    def isEmpty(self): return len(self.top)==0 #계산 결과가 True, False
    def size(self): return len(self.top)
    def clear(self): self.top=[] #주의: 이제 전역변수 선언이 필요없음

    def push(self, item): 
        self.top.append(item) #리스트의 맨 뒤에 item 추가

    def pop(self):
        if not self.isEmpty(): #공백상태가 아니면
            return self.top.pop(-1) #리스트의 맨 뒤에서 항목을 하나 꺼내고 반환
        
    def peek(self): #맨 위의 항목을 삭제하지 않고 반환
        if not self.isEmpty(): #공백상태가 아니면
            return self.top[-1] #맨 뒷 항목을 반환(삭제하지 않음)
    
    def __str__(self):
        return str(self.top[::-1]) #역순으로 출력, 최근의 항목을 먼저

odd=Stack() #홀수 저장을 위한 스택
even=Stack() #짝수 저장을 위한 스택
 
for i in range(10): #i=0, 1, 2,..., 9
    if i%2==0: even.push(i) #짝수는 even에 push
    else: odd.push(i) #홀수는 even에 push

print(' 스택 even push 5회: ', even.top) #even 스택 출력
print(' 스택 odd push 5회: ', odd.top) #odd 스택 출력
print(' 스택 even peek: ', even.peek()) #even 스택에서 두 번 pop()
print(' 스택 odd peek: ', odd.peek()) #odd 스택에서 세 번 pop()

for _ in range(2): even.pop() #even 스택에서 두 번 pop()
for _ in range(3): odd.pop() #odd 스택에서 세 번 pop()
print(' 스택 even pop 2회: ', even.top) #even 스택 출력
print(' 스택 odd pop 3회: ', odd.top) #odd 스택 출력
