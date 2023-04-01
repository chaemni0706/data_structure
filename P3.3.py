class Set: #Set 클래스 정의
    def __init__(self): #__init__ 메소드 정의
        self.items=[] #items 빈리스트 생성
    def size(self): #size 메소드 정의
        return len(self.items) #items 리스트의 길이 반환
    def display(self, msg): #display 메소드 정의
        print(msg, self.items) #msg, items 리스트 출력
    def contains(self, item): #contains 메소드 정의
        for i in range(len(self.items)): #item이 items리스트에 있는지 확인
            if self.items[i]==item:
                return True
        return False
    def insert(self, elem): #insert 메소드 정의 
        if elem not in self.items: #elem이 items 리스트에 없으면 리스트에 추가
            self.items.append(elem) 
    def delete(self, elem): #delete 메소드 정의
        if elem in self.items: #ellem이 items리스트에 있으면 리스트에서 삭제
            self.items.remove(elem)
    def union(self, setB): #union 메소드 정의
        setC=Set() 
        setC.items=list(self.items)
        for elem in setB.items:
            if elem not in self.items:
                setC.items.append(elem)
        return setC
    def intersect(self, setB): #intersect 메소드 정의
        setC=Set()
        for elem in setB.items:
            if elem in self.items:
                setC.items.append(elem)
        return setC
    def difference(self,setB): #differce 메소드 정의
        setC=Set()
        for elem in self.items:
            if elem not in setB.items:
                setC.items.append(elem)
        return setC
    
setA=Set() #setA 객체 생성
setA.insert('휴대폰') #insert메소드 사용하여 items 리스트에 휴대폰, 지갑, 손수건 추가
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:') #display 메소드 사용하여 Set A:와 items 리스트 출력

setB=Set()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')
setA.union(setB).display('A U B:') #setA객체와 setB객체의 합집합을 구한 후 display 메소드를 사용하여 A U B:와 items 리스트를 출력
setA.intersect(setB).display('A^B:') #교집합 구함->출력
setA.difference(setB).display('A-B:') #차집합 구함->출력