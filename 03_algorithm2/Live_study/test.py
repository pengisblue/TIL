for i in range(7, -1, -1):
    print(int(bool(-1 & (i << 1))), end='')
print(bin(-1))