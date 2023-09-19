# 9/19 강의
## 백트래킹
```python
# 많이 작성되는 형태
def func():
    # 재귀를 끝내는 기저 조건

    # 가지치기

    # 반복문
        # 가지치기

        # 재귀 들어가기 전
        # 재귀 함수 호출
        # 돌아와서 초기화
```

## 트리
- 사이클이 없는 연결그래프
    > 연결그래프: 모든 꼭짓점이 서로 갈 수 있다
### 이진 트리
- 자녀 노드가 둘 이하인 트리
#### 이진 트리 종류
- 완전 이진 트리
    - 마지막 레벨을 제외한 모든 레벨은 꽉 차있어야 한다.
    - 마지막 레벨 노드는 왼쪽부터 채워져야 한다.
- 포화 이진 트리
    - 모든 레벨이 꽉 차 있는 것
- 나머지 이진 트리
#### 순회 방법
- 전위
    - 부모 -> 좌 -> 우
- 중위
    - 좌 -> 부모 -> 우
- 후위
    - 좌 -> 우 -> 부모
#### 트리 저장 방법
- 이진 트리 저장
    - 일차원 배열 저장
- 연결 리스트 저장
```python
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

nodes[1].preorder()     # 1 2 4 3 5 6 
print()
nodes[1].inorder()      # 4 2 1 5 3 6
print()
nodes[1].postorder()    # 4 2 5 6 3 1
```
- 인접 리스트 저장

## 힙(heap)