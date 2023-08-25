import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    move = [0, 1, -1]
    result = 0
    table.insert(0, [9] * 100)
    table.append([9] * 100)
    # print(list(map(list, map(''.join, list(zip(*table))))))
    for j in range(N):
        i = 1
        while i <= N:
            if table[i][j]:
                row = move[table[i][j]]
                di = i + row
                while table[di][j] == 9:
                    if table[di][j] == table[i][j]:
                        table[i][j] = 0
                        i = di + 1
                        break
                    elif table[di][j] and table[di][j] != table[i][j]:
                        table[i][j], table[di-row][j] = table[di-row][j], table[i][j]
                        result += 1
                        i = di + 1
                        break
                    di += row
                else:
                    table[i][j] = 0
                    i = N + 1
    print(result)