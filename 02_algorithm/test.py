N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
'''
3
1 2 3
4 5 6
7 8 9
'''
for i in range(3):
    for j in range(i+1, 3):
        if i < j:  # 조건이 없으면 원래대로 돌아감
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]