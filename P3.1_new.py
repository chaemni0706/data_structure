items=[]

def insert(pos, elem):
    items.append(None) # None 값을 추가하여 리스트 크기를 1 증가시킴
    for i in range(size()-1, pos, -1):
        items[i] = items[i-1] # 삽입 위치 이후의 항목들을 모두 한 칸씩 뒤로 이동
    items[pos] = elem # 새로운 항목 삽입
def delete(pos):
    global items
    for i in range(pos+1, len(items)):
        items[i-1] = items[i] # 이후의 항목들을 한 칸씩 앞으로 이동
    return items.pop(-1) # 마지막 항목을 삭제하고 반환
def getEntry(pos): return items[pos] #pos번째 항목 반환
def isEmpty():
    if len(items)==0: #크기가 0이면
        return True #True를 반환
    else: #크기가 0이 아니면
        return False #False를 반환
def isEmpty(): return len(items)==0 #크기가 0이면 True 아니면 False
def size(): return len(items) #리스트의 크기 반환, len() 함수 이용
def clear(): 
    global items #items가 전역변수임을 지정
    items=[] #전역변수 items를 초기화
def find(item):
    global items
    for i in range(len(items)):
        if items[i] == item:
            return i # 항목을 찾으면 인덱스 반환
    return -1 # 항목을 찾지 못하면 -1 반환

def replace(pos, elem): items[pos]=elem #pos번째 항목 변경
def sort(): items.sort() #정렬(sort메소드 이용)
def merge(lst): #'lst'를 인자로 받아 merge 정의
    for i in range(len(lst)):
        insert(size(), lst[i]) # lst의 모든 항목을 items의 끝에 순서대로 추가
def display(msg='ArrayList:' ): #msg를 인자로 받아 리스트의 크기와 항목을 출력하는 함수 display 정의
    print(msg, size(), items) 

display('파이썬 리스트로 구현한 리스트 테스트') #display 함수 호출
insert(0, 10); insert(0, 20); insert(1, 30) #리스트의 앞에 10, 20, 30 삽입
insert(size(), 40); insert(2, 50) #리스트의 끝에 40삽입, 인덱스 2에 50 삽입
display("파이썬 리스트로 구현한 List(삽입*5): ") 
sort() #리스트 정렬
display("파이썬 리스트로 구현한 List(정렬후): ")
replace(2, 90) #인덱스 2에 해당하는 걸 90으로 교체
display("파이썬 리스트로 구현한 List(교체*1): ")
delete(2); delete(size()-1); delete(0) #인덱스2, 리슽트 마지막 항목, 리스트의 첫번째 항목 삭제

display("파이썬 리스트로 구현한 List(삭제*3): ")
lst=[1, 2, 3] #새로운 리스트 생성->[1, 2, 3]으로 초기화
merge(lst)
display("파이썬 리스트로 구현한 List(병합+3):")
clear()
display("파이썬 리스트로 구현한 List(정리후): ")