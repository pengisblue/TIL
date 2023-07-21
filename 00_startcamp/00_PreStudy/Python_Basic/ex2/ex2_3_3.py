low, high = map(int, input().split())
datas = list(map(int, input().split()))

for data in datas:
    if low <= data <= high:
        print('Nothing to report')
    elif data == -999:
        break
    else:
        print('Alert!')
        break