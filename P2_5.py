class Bag: #class 정의
    def __init__(self): #메소드 생성
        self.items=[] #items 리스트 생성
    def insert(self, item): #insert 메소드 생성
        self.items.append(item) #items 리스트에 인자로 받은 item 추가
    def remove(self, item): #remove 메소드 생성
        self.items.remove(item) #items 리스트에서 인자로 받은 item 삭제
    def __str__(self): #__str__ 메소드 생성
        return f'가방속의 물건: {", ".join(self.items)}' #가방 속 물건을 문자열로 반환

myBag=Bag() #myBag객체 생성, 
myBag.insert('휴대폰') #Bag에 폰 삽입
myBag.insert('지갑') #Bag에 지갑 삽입
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print(myBag) #myBag 객체 출력
 
myBag.insert('빗') #myBag 객체에 insert 메소드를 사용하여 빗을 삽입
myBag.remove('손수건') #myBag 객체에 remove 메소드를 사용하여 손수건을 삭제
print(myBag) #myBag 객체 출력

