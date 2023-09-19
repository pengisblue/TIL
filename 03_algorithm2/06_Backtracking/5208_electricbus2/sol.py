import sys
sys.stdin = open('input.txt')


def backtracking():

    pass


T = int(input())
for tc in range(1, T+1):
    M = list(map(int, input().split()))
    N = M[0]
    charge = 0
