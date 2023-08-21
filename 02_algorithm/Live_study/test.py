'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(node):
    if node != 0:   # 존재하는 정점이면
        print(node, end=' ')    # visit(n)
        preorder(left[node])    # 왼쪽 서브트리로 이동
        preorder(right[node])    # 오른쪽 서브트리로 이동


def inorder(node):
    if node != 0:   # 존재하는 정점이면
        preorder(left[node])    # 왼쪽 서브트리로 이동
        print(node, end=' ')    # visit(n)
        preorder(right[node])    # 오른쪽 서브트리로 이동


def postorder(node):
    if node != 0:   # 존재하는 정점이면
        preorder(left[node])    # 왼쪽 서브트리로 이동
        preorder(right[node])    # 오른쪽 서브트리로 이동
        print(node, end=' ')    # visit(n)


V = int(input())    # 정점수 = 마지막 정점 번호
E = V - 1           # 트리의 간선 수 = 정점 수 -1
edge = list(map(int, input().split()))
# 부모를 인덱스로 자식을 저장
left = [0] * (V+1)
right = [0] * (V+1)
# 자식을 인덱스로 부모를 저장
parent = [0] * (V+1)
# [왼쪽, 오른쪽, 부모]
tree = [[0] * 3 for _ in range(V+1)]

for i in range(E):
    p, c = edge[i*2], edge[i*2+1]
    if left[p] == 0:     # 자식1이 아직 없으면
        left[p] = c
    else:
        right[p] = c
    parent[c] = p

    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p

print(tree)     
# [[0, 0, 0], [2, 3, 0], [4, 0, 1], [5, 6, 1], [7, 0, 2], [8, 9, 3], [10, 11, 3], [12, 0, 4], [0, 0, 5], [0, 0, 5], [0, 0, 6], [13, 0, 6], [0, 0, 7], [0, 0, 11]]

# 루트 찾기1
root = 0
for i in range(1, V+1):
    if parent[i] == 0:
        root = i
        break

# 루트 찾기2
# root = 1 
# while parent[root] != 0:
#     root += 1

print('전위순회')
preorder(root)
print()
print('중위순회')
inorder(root)
print()
print('후위순회')
postorder(root)