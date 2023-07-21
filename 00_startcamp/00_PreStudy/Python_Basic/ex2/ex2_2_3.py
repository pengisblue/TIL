N = int(input())
result = str(N)
if N >= 1000000000000000000000000:
    result = str(N // 1000000000000000000000000) + 'Y'
elif N >= 1000000000000000000000:
    result = str(N // 1000000000000000000000) + 'Z'
elif N >= 1000000000000000000:
    result = str(N // 1000000000000000000) + 'E'
elif N >= 1000000000000000:
    result = str(N // 1000000000000000) + 'P'
elif N >= 1000000000000:
    result = str(N // 1000000000000) + 'T'
elif N >= 1000000000:
    result = str(N // 1000000000) + 'G'
elif N >= 1000000:
    result = str(N // 1000000) + 'M'
elif N >= 1000:
    result = str(N // 1000) + 'k'
elif N >= 0:
    pass
print(result)