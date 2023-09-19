class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    # 삽입함수
    def insert(self, childNode):
        # 왼쪽 자식이 없을 경우
        if not self.left:
            self.left = childNode
            return

        # 오른쪽 자식이 없을 경우
        if not self.right:
            self.right = childNode
            return
        
        return

    # 순회
    def preorder(self):
        # 값이 있을 때
        if self != None:
            print(self.value, end = ' ')
            # 왼쪽이 있다면 왼쪽 자식 조회
            if self.left:
                self.left.preorder()
            # 오른쪽이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.preorder()
    
    
    def inorder(self):
        # 값이 있을 때
        if self != None:
            # 왼쪽이 있다면 왼쪽 자식 조회
            if self.left:
                self.left.inorder()

            print(self.value, end = ' ')

            # 오른쪽이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.inorder()
    
    
    def postorder(self):
        # 값이 있을 때
        if self != None:
            # 왼쪽이 있다면 왼쪽 자식 조회
            if self.left:
                self.left.postorder()
            # 오른쪽이 있다면 오른쪽 자식 조회
            if self.right:
                self.right.postorder()

            print(self.value, end = ' ')


arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6]
# 이진 트리 만들기
nodes = [TreeNode(i) for i in range(0, 14)]
for i in range(0, len(arr), 2):
    parentNode = arr[i]
    childNode = arr[i + 1]
    nodes[parentNode].insert(nodes[childNode])

nodes[1].preorder()
print()
nodes[1].inorder()
print()
nodes[1].postorder()