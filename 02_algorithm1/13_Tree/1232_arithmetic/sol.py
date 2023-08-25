import sys
sys.stdin = open('input.txt')


def postorder(node):
    if type(tree[node][0]) == int:
        return tree[node][0]
    else:
        left = postorder(tree[node][1])
        right = postorder(tree[node][2])

        if tree[node][0] == '+':
            return left + right
        elif tree[node][0] == '-':
            return left - right
        elif tree[node][0] == '*':
            return left * right
        elif tree[node][0] == '/':
            return left // right


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)]
    for _ in range(N):
        info = list(input().split())
        index = int(info[0])
        if info[1].isdigit():
            tree[index][0] = int(info[1])
        else:
            tree[index][0] = info[1]
            tree[index][1] = int(info[2])
            tree[index][2] = int(info[3])

    print(f'#{tc}', postorder(1))
