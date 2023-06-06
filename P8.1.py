class TNode:
    def __init__ (self, data, left, right):
        self.data=data
        self.left=left
        self.right=right

MAX_QSIZE=10

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE

    def enqueue(self, item):
        node = TNode(item, None, None)
        if self.isEmpty():
            node.left = node
            self.tail = node
        else:
            node.left = self.tail.left
            self.tail.left = node
        self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % MAX_QSIZE
            return data
    
    def isEmpty(self):
        return self.front == self.rear



def preorder(n):
    if n is not None:
        print(n.data, end=" ")
        preorder(n.left)
        preorder(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root):
    queue=CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n=queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def count_node(n):
    if n is None:
        return 0
    else:
        return 1+count_node(n.left)+count_node(n.right)
    
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left)+count_leaf(n.right)
    
def calc_height(n):
    if n is None:
        return 0
    hLeft=calc_height(n.left)
    hRight=calc_height(n.right)
    if (hLeft>hRight):
        return hLeft+1
    else:
        return hRight+1

d=TNode('D', None, None)
b=TNode('B', d, None)
g=TNode('G', None, None)
h=TNode('H', None, None)
e=TNode('E', g, h)
f=TNode('F', None, None)
c=TNode('C', e, f)
root=TNode('A', b, c)

print('\n In-Order: ', end='')
inorder(root)
print('\n Pre-Order: ', end='')
preorder(root)
print('\n Post-Order: ', end='')
postorder(root)
print('\n Level-Order: ', end='')
levelorder(root)
print()

print("노드의 개수=%d개" %count_node(root))
print("단말의 개수=%d개" %count_leaf(root))
print("트리의 높이=%d"%calc_height(root))