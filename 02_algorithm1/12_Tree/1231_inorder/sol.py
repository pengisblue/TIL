import sys
sys.stdin = open('input.txt')


def inorder(node):
    if node != 0:
        inorder(tree[node][1])
        print(tree[node][0], end='')
        inorder(tree[node][2])


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)]
    for _ in range(N):
        info = list(input().split())
        for i in range(1, len(info)):
            if i > 1:
                info[i] = int(info[i])
            tree[int(info[0])][i-1] = info[i]

    print(f'#{tc}', end=' ')
    inorder(1)
    print()
