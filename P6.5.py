class Term: #다항식의 항을 나타내는 클래스
    def __init__(self, expo, coef):
        self.expo = expo #항의 지수
        self.coef = coef #항의 개수
        
class Node: #단순연결리스트를 위한 노드 클래스
    def __init__(self, elem, prev=None, neext=None): #생성자, 디폴트 인수 사용
        self.data = elem #데이터 멤버 생성 및 초기화
        self.prev = prev #Prev 생성 및 초기화
        self.next = next #next 생성 및 초기화

class LinkedList: #연결된 리스트 클래스
    def __init__(self): 
        self.head = None

    def insert(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node #맨앞에 new_node 삽입

class SparsePoly(LinkedList): #희소 다항식 클래스
    def __init__(self):
        LinkedList.__init__(self)

    def __add__(self, other): #다항식 덧셈 함수
        result = SparsePoly()
        current1, current2 = self.head, other.head
        while current1 and current2:
            if current1.data.expo == current2.data.expo:
                result.insert(Term(current1.data.expo, current1.data.coef + current2.data.coef))
                current1 = current1.next
                current2 = current2.next
            elif current1.data.expo > current2.data.expo:
                result.insert(Term(current1.data.expo, current1.data.coef))
                current1 = current1.next
            else:
                result.insert(Term(current2.data.expo, current2.data.coef))
                current2 = current2.next
        while current1:
            result.insert(Term(current1.data.expo, current1.data.coef))
            current1 = current1.next
        while current2:
            result.insert(Term(current2.data.expo, current2.data.coef))
            current2 = current2.next
        return result