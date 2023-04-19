items = []			       

def insert(pos, elem) :		
   items.insert(pos, elem)	

def delete(pos) :		   
   items.pop(pos)		   

def getEntry(pos): 
    return items[pos]	

def isEmpty( ):
    if len(items) == 0 :
        return True		
    else :				
        return False	

def size( ):	    
    return len(items)	
def clear( ):      
    global items
    items = []		       

def find(item) : 
    return items.index(item)	
def replace(pos, elem): 
    items[pos] = elem	
def sort():
    for i in range(1, len(items)):
        key = items[i]
        j = i - 1
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key			
def merge(lst) : 
    items.extend(lst)	

def display(msg='ArrayList:' ):		
    print(msg, size(), items)		


display('테스트')
insert(0, 10);		insert(0, 20);    insert(1, 30)
insert(size(), 40);	insert(2, 50)
display("List(삽입x5): ")
sort()
display("List(정렬후): ")
replace(2, 90)
display("List(교체x1): ")
delete(2);	delete(size() - 1);	delete(0)
display("List(삭제x3): ")
lst = [ 1, 2, 3 ]
merge(lst)
display("List(병합+3): ")
clear()
display("List(정리후): ")
