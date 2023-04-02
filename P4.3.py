class Stack:
    def __init__(self): #생성자 
        self.top = [] #top이 이제 클래스의 멤버 변수가 됨
        
    def push(self, item): #push 연산 
        self.top.append(item) #리스트의 맨 뒤에서 항목을 하나 꺼내고 반환
    
    def pop(self): #pop 연산
        if not self.isEmpty(): #공백 상태가 아니면 
            return self.top.pop() #리스트의 맨 뒤에서 항목을 하나 꺼내고 반환
        else:
            return None
    
    def isEmpty(self): #스택이 비어있는지 확인 
        return len(self.top) == 0 #계산 결과가 True, False
    
        
def checkBrackets(statement): #statement에 들어온 문자열의 괄호 짝이 맞는지 확인 
    stack = Stack() #객체 생성 
    line = 1 #현재 라인을 나타내는 변수 초기화 
    char = 0 #현재 문자 위치를 나타내는 변수 초기화 
    for ch in statement: #문자열의 각 문자에 대해 반복 
        char += 1 #문자 위치 증가 
        if ch == '\n': #개행 문자인 경우 
            line += 1 #라인 수 증가 
            char = 0 #문자 위치를 0으로 초기화 
        if ch in ('{', '[', '('): #여는 괄호인 경우 
            stack.push((ch, line, char)) #현재 위치와 함께 저장 
        elif ch in ('}', ']', ')'): #닫는 괄호인 경우 
            if stack.isEmpty(): #스택이 비어있는 경우 
                return ("매칭되는 괄호가 없음", line, char) #조건 2에 위반
            else:
                left = stack.pop() #스택의 맨 위에 있는 괄호를 꺼내서 left에 저장 
                if (ch == "}" and left[0] != "{") or \
                        (ch == "]" and left[0] != "[") or \
                        (ch == ")" and left[0] != "("):
                    return ("괄호가 다름", line, char) #조건 3에 위반
                
    if stack.isEmpty(): #스택이 비어있는 경우 
        return 0 #괄호 짝이 맞음 
    else:
        left = stack.pop() #스택에 남아있는 여는 괄호를 꺼내서 left에 저장 
        return ("매칭되지 않는 여는 괄호", left[1], left[2]) #조건 1에 위반
    
        
def checkFile(filename): #파일 내용에 대한 괄호 검사 수행 
    with open(filename, 'r') as f: #파일을 읽기 모드로 열기 
        statement = f.read() #파일 내용을 문자열로 읽어오기 
    result = checkBrackets(statement) #괄호 검사
