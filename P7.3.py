class Set:				        
    def __init__( self ):		
        self.items = []			

    def size( self ): 			
        return len(self.items)	
    def display(self, msg):		
        print(msg, self.items)	

    def contains(self, item) :
        for i in range(len(self.items)):
            if self.items[i] == item :	
                return True
        return False		

    def insert(self, elem) :
        if elem not in self.items :
           self.items.append(elem)

    def delete(self, elem) :
        if elem in self.items :
           self.items.remove(elem)

    def union( self, setB ):		    
        setC = Set()			        
        setC.items = list(self.items)	
        for elem in setB.items :	    
            if elem not in self.items :	
                setC.items.append(elem)	
        return setC			            

    def intersect( self, setB ):	
        setC = Set()
        for elem in setB.items :	
            if elem in self.items :	
                setC.items.append(elem)	
        return setC

    def difference( self, setB ):	    
        setC = Set()
        for elem in self.items:		    
            if elem not in setB.items:	
                setC.items.append(elem)	
        return setC

setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A:')

setB = Set()
setB .insert('빗')
setB .insert('파이썬 자료구조')
setB .insert('야구공')
setB .insert('지갑')
setB.display('Set B:')

setB.insert('빗')
setA.delete('손수건')
setA.delete('발수건')
setA.display('Set A:')
setB.display('Set B:')

setA.intersect(setB).display('A ^ B:') #교집합

def insert(self, elem) :                
    if elem in self.items : 
        return      
    for idx in range(len(self.items)) : 
        if elem < self.items[idx] :     
            self.items.insert(idx, elem)
            return
    self.items.append(elem)             


    def __eq__( self, setB ):       	
        if self.size() != setB.size() :	
            return False
        for idx in range(len(self.items)): 			
            if self.items[idx] != setB.items[idx] :	
                return False
        return True

    def union(self, setB):
        newSet = Set()
        i, j = 0, 0
        while i < len(self.items) and j < len(setB.items):
            if self.items[i] < setB.items[j]:
                newSet.items.append(self.items[i])
                i += 1
            elif setB.items[j] < self.items[i]:
                newSet.items.append(setB.items[j])
                j += 1
            else:
                newSet.items.append(self.items[i])
                i += 1
                j += 1
        while i < len(self.items):
            newSet.items.append(self.items[i])
            i += 1
        while j < len(setB.items):
            newSet.items.append(setB.items[j])
            j += 1
        return newSet
