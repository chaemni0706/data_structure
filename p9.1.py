class Node: #이진 탐색 트리의 노드를 나타내는 클래스
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_minimum(node): #이진 탐색 트리에서 최소 키를 찾는 함수
    if node is None:
        return None

    while node.left is not None:
        node = node.left

    return node.key

def find_maximum(node): #이진 탐색 트리에서 최대 키를 찾는 함수
    if node is None:
        return None

    while node.right is not None:
        node = node.right

    return node.key


root = Node(8) #트리 생성
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)


minimum = find_minimum(root) #최소 키 찾기
print("최소 키:", minimum)

maximum = find_maximum(root) #최대 키 찾기
print("최대 키:", maximum)
