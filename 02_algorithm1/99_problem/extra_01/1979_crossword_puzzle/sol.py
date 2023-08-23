import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())    # 퍼즐 길이, 단어 길이
    puzzle = [input().replace(' ', '') for i in range(N)]
    puzzle.extend(list(map(lambda x: ''.join(x), list(zip(*puzzle)))))  # 세로행
    
    blanks = list(map(lambda x: x.split('0'), puzzle))  # '1'만 남기기
    # blanks = [i.split('0'), for i in puzzle]
    result = 0
    for i in range(len(blanks)):
        result += blanks[i].count('1'*K)    # '1'의 길이 = 빈칸 길이

    print(f'#{tc} {result}')
