class Node: #이진 탐색 트리의 노드를 나타내는 클래스
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def search_bst_iter(root, key): #주어진 키를 이진 탐색 트리에서 반복적으로 탐색하여 해당 노드를 반환하거나, 키가 존재하지 않을 경우 None을 반환
    while root is not None:
        if key < root.key:
            root = root.left
        elif key > root.key:
            root = root.right
        else:
            return root

    return None

def insert_bst(root, key): #주어진 키를 이진 탐색 트리에 삽입
    if root is None:
        root = Node(key)
        return root

    current = root
    while True:
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
                break
            else:
                current = current.left
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
                break
            else:
                current = current.right
        else: #키가 이미 존재하는 경우            
            break

    return root

root = Node(8) #트리 생성
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)

def inorder_traversal(node): #트리 순회
    if node:
        inorder_traversal(node.left)
        print(node.key, end=" ")
        inorder_traversal(node.right)

print("트리 순회 결과:")
inorder_traversal(root)
print()

insert_bst(root, 5) #삽입 연산
insert_bst(root, 9)

print("트리 순회 결과 (삽입 후):")
inorder_traversal(root)
print()
