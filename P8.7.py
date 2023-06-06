class Maxheap: #최대 힙 클래스
    def __init__(self): #생성자
        self.heap=[] #리스트(배열)을 이용한 힙
        self.heap.append(0) #0번 항목은 사용하지 않음

    def size(self): return len(self.heap) - 1 #힙의 크기
    def isEmpty(self): return self.size() == 0 #공백 검사
    def Parent(self, i): return self.heap[i//2] #부모 노드 반환
    def Left(self, i): return self.heap[i*2] #왼쪽 자식 반환
    def Right(self, i): return self.heap[i*2+1] #오른쪽 자식 반환 
    def display(self, msg = '힙 트리: '):
        print(msg, self.heap[1:]) #파이썬 리스트의 슬라이싱 이용
    def insert(self, n):
        self.heap.append(n) #맨 마지막 노드로 일단 삽입
        i=self.size()#노드 n의 위치
        while (i != 1 and n> self.Parent(i)): #부모보다 큰 동안 계속 업힙
            self.heap[i] = self.Parent(i) #부모를 끌어내림
            i = i//2 #i를 부모의인덱스로 올림
        self.heap[i] = n #마지막 위치에 n 삽입
    def delete(self):
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot=self.heap[1] #삭제할 루트를 복사해 둠
            last=self.heap[self.size()] #마지막 노드
            while (child <= self.size()): #마지막 노드 이전까지
                if child<self.size() and self.Left(parent)<self.Right(parent): #만약 오른쪽 노드가 더 크면 child를 1증가
                    child+=1
                if last >= self.heap[child]: #더 큰 자식이 더 작으면
                    break #삽입 위치를 찾음, 다운 힙 종료
                self.heap[parent] = self.heap[child] #아니면 다운힙 계속
                parent=child
                child*=2

            self.heap[parent]=last #맨 마지막 노드를 parent위치에 복사
            self.heap.pop(-1) #맨 마지막 노드 삭제
            return hroot  #저장해두었던 루트 반환
def isMaxHeapRecur(A, i):#노드가 리프이면 최대 힙
    if i > len(A)//2:
        return True
   
    if A[i] >= A[2*i] and (2*i+1 >= len(A) or A[i] >= A[2*i+1]): #현재 노드의 힙 속성을 확인
        return isMaxHeapRecur(A, 2*i) and isMaxHeapRecur(A, 2*i+1) #왼쪽 및 오른쪽 자식에 대한 힙 속성을 재귀적으로 확인
    else:
        return False    

def isMinHeapRecur(A, i): #노드가 리프이면 최소 힙      
        if i > len(A)//2:
            return True
        if A[i] <= A[2*i] and (2*i+1 >= len(A) or A[i] <= A[2*i+1]): #현재 노드의 힙 속성을 확인    
            return isMinHeapRecur(A, 2*i) and isMinHeapRecur(A, 2*i+1) #왼쪽 및 오른쪽 자식에 대한 힙 속성을 재귀적으로 확인
        else:
            return False 
        