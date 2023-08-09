def fibo(n):
    global memo
    if n >= 2 and memo[n] == 0:
        memo[n] = (fibo(n-1) + fibo(n-2))
    return memo[n]
n = 0
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo(0))
print(memo)