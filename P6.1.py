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

    def peek(self): #연결된 스택의 peek 연산
        if not self.isEmpty(): #공백 아니면
            return self.top.data #시작 항목의 데이터 반환
        else:
            return None

def isPal(s):
    stack = [] #스택 초기화
   
    for c in s: #스택에 문자열 저장
        if c.isalnum():
            stack.append(c.lower())  #소문자로 변환
    
    reversed_s = ''.join(stack[::-1]) #스택에 저장된 문자열 뒤집음
    
    return s.lower() == reversed_s.lower() #문자열과 뒤집은 문자열이 같은지 비교

s = input("문자열을 입력하세요: ") #문자열 입력
if isPal(s):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")