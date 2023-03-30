class ArrayList: #ArrayList 클래스 정의
    def __init__(self): #클래스 초기화, 빈 리스트 생성
        self.items=[]
    def insert(self, pos, elem): #pos에 elem 삽입
        self.items.insert(pos, elem)
    def delete(self, pos): #pos의 elem을 삭제하고 반환
        return self.items.pop(pos)
    def isEmpty( self ): #리스트가 비어있는지 여부를 반환
        return self.size()==0 
    def getEntry(self,pos): #pos의 elem 반환
        return self.items[pos]
    def size(self): #리스트의 길이 반환
        return len(self.items)
    def find(self, item): #리스트에서 item을 찾아 해당 위치 반환
        return self.items.index(item)
    def replace(self, pos, elem): #pos의 요소를 새로운 elem으로 교체
        self.items[pos]=elem
    def sort(self): #리스트를 오름차순으로 정렬
        self.items.sort()
    def merge(self, lst): #리스트에 다른 리스트 추가
        self.items.extend(lst)
    def display(self, msg='ArrayList:' ): #리스트 출력
        print(msg, self.size(), self.items)

def myLineEditor(): #텍스트 파일 편집
    list=ArrayList() 
    while True: #무한 루프
        command=input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, 1-파일읽기, s-저장, q-종료, f-문자열을 포함하고 있는 라인들만 출력=> ") #명령어 입력

        if command=='i': #i=입력, 삽입할 행의 번호와 내용을 입력받고 클래스의 insert호출해서ㅓ 내용 삽입
            pos=int(input(" 입력행 번호: "))
            str=input(" 입력행 내용: ")
            list.insert(pos, str)
        elif command=='d': #d=삭제, 삭제할 행의 번호를 입력받고 클래스의 delete 호출해서 내용 삭제
            pos=int(input(" 삭제행 번호: "))
            list.delete(pos)
        elif command=='r': #r=변경, 변경할 행 번호와 내용 입력받고 클래스의 replace 메소드를 호출해서 새로운 값으로 변경
            pos=int(input(" 변경행 번호"))
            str=input(" 변경행 내용: ")
            list.replace(pos, str)
        elif command=='q': return #q=종료, 함수 종료
        elif command=='p': #p=출력, 클래스의 size, getEntry메소드를 이용해서 리스트 전체 출력
            print('Line Editor')
            for line in range(list.size()):
                print('[%2d] '%line, end='')
                print(list.getEntry(line))
            print()
        elif command=='l': #l=파일 읽기 명령, 파일 이름을 입력받고 클래스의 insert 메소드를 이용해 리스트에 추가
            filename=input("파일이름: ")
            infile=open(filename, "r")
            lines=infile.readlines()
            for line in lines:
                list.insert(list.size(), line.rstrip('\n'))
            infile.close()
        elif command=='s': #s=파일 저장, 파일 이름을 입력받고 클래스의 size, getEntry 메소드를 이용해 리스트 전체를 파일에 저장
            filename=input("파일이름: ")
            outfile=open(filename, "w")
            for i in range(list.size()): 
                outfile.write(list.getEntry(i)+'/n/')
            outfile.close()
        elif command=='f': #f=검색, 검색할 문자열을 입력받고 클래스의 getEntry 메소드를 이용해 해당 문자열을 포함하는 모든 행 출력
            str=input("검색할 문자열 입력: ")
            for line in range(list.size()):
                if str in list.getEntry(line):
                    print('[%2d] '%line, end='')
                    print(list.getEntry(line))
            print()
myLineEditor()