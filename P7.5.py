class Entry:
    def __init__( self, key, value ):
        self.key = key
        self.value = value

    def __str__( self ):
        return str("%s:%s"%(self.key, self.value) )
    
def sequential_search(A, key, low, high) :	
    for i in range(low, high+1) :			
        if A[i].key == key :  				
            return i 						
    return None							    


def binary_search(A, key, low, high) :
	if (low <= high) :				        
		middle = (low + high) // 2	        
		if key == A[middle].key :		    
			return middle
		elif (key<A[middle].key) :	        
			return binary_search(A, key, low, middle - 1)
		else :						
			return binary_search(A, key, middle + 1, high)
	return None        				

def binary_search_iter(A, key, low, high) :
	while (low <= high) :       		
		middle = (low + high) // 2
		if key == A[middle].key:	    
			return middle
		elif (key > A[middle].key):	
			low = middle + 1		
		else:						
			high = middle - 1		
	return None      				

class BinaryMap:
    def __init__(self):
        self.table = []

    def size(self):
        return len(self.table)

    def display(self, msg):
        print(msg)
        for entry in self.table:
            print("  ", entry)

    def insert(self, key, value):
        index = self.binary_search_index(key, 0, self.size()-1)
        self.table.insert(index, Entry(key, value))

    def binary_search_index(self, key, low, high):
        if low > high:
            return low
        else:
            middle = (low + high) // 2
            if key == self.table[middle].key:
                return middle
            elif key < self.table[middle].key:
                return self.binary_search_index(key, low, middle - 1)
            else:
                return self.binary_search_index(key, middle + 1, high)

    def search(self, key):
        return self.binary_search(key, 0, self.size()-1)

    def sequential_search(A, key, low, high) :	
        for i in range(low, high+1) :			
            if A[i].key == key :  				
                return i 						
        return None							    


    def binary_search(A, key, low, high) :
        if (low <= high) :				        
            middle = (low + high) // 2	        
            if key == A[middle].key :		    
                return middle
            elif (key<A[middle].key) :	        
                return binary_search(A, key, low, middle - 1)
            else :						
                return binary_search(A, key, middle + 1, high)
        return None        				

    def binary_search_iter(A, key, low, high) :
        while (low <= high) :       		
            middle = (low + high) // 2
            if key == A[middle].key:	    
                return middle
            elif (key > A[middle].key):	
                low = middle + 1		
            else:						
                high = middle - 1		
        return None        				

    def delete(self, key):
        index = self.binary_search_index(key, 0, self.size()-1)
        if index < self.size() and self.table[index].key == key:
            self.table.pop(index)

map = BinaryMap()						
map.insert('data', '자료')					
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')	
map.display("나의 단어장: ")			

print("탐색:game --> ", map.search('game'))	
print("탐색:over --> ", map.search('over'))
print("탐색:data --> ", map.search('data'))

map.delete('game')						
map.display("나의 단어장: ")

