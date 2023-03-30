top=[]

def isEmpty():
    return len(top)==0

def push(item):
    top.append(item)

def pop():
    if not isEmpty():
        return top.pop(-1)
    
def peek():
    if not isEmpty():
        return top[-1]
    
def size(): return len(top)
def clear():
    global top
    top=[]

for i in range(1, 6):
    push(i)
print(' push 5회: ', top)
print('')