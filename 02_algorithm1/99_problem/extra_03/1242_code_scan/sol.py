import sys
sys.stdin = open('input.txt')

code = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

# hex_to_bin = {대문자, 숫자로 표현된 16진수: 4자리까지 표현한 2진수}
hex_to_bin = {hex(i).replace('0x', '').upper(): f'{i:04b}' for i in range(16)}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 행, 열
    arr = set(input().strip() for _ in range(N))
    arr = list(arr)
    # empty = '0' * M
    # del arr[arr.index(empty)]   # 빈 문자 제거
    for i in range(len(arr)):
        tmp = ''
        for j in arr[i]:
            tmp += hex_to_bin[j]
        arr[i] = tmp

    M *= 4  # 4자리 2진수로 바꼈으므로 길이도 4배
    codes = set()  # 암호코드만 잘라서 보관
    result = 0  # 올바른 암호코드 계산값 담아둘 곳
    for i in range(len(arr)):
        idx = len(arr[i]) - 1
        cnt_1, cnt_0 = 0, 0
        while idx >= 49:
            # 암호 코드 맨 끝 인덱스
            if cnt_1 == 0 and arr[i][idx] == '1':
                e_idx = idx
                cnt_1 = 1
            if arr[i][idx] == '0' and arr[i][idx-1] == '1':
                cnt_0 += 1
            # 마지막 암호코드의 길이로 코드의 두께(mul)를 구한 뒤 이를 바탕으로
            # 코드의 전체 길이와 시작 인덱스 구하기
            if cnt_0 == 3:
                one_idx = idx   # 암호 코드 마지막 자리 시작 인덱스
                LEN = e_idx - (one_idx-1)   # 암호 코드의 길이
                mul = LEN // 7  # 코드의 두께
                # 암호코드 시작 인덱스
                s_idx = e_idx - (LEN*8) + 1
                # 시작부터 끝까지 두께만큼 건너뛰면서 실제 코드를 구한 후 리스트에 추가
                codes.add(arr[i][s_idx:e_idx+1:mul])
                cnt_1 = 0
                cnt_0 = 0
                idx = s_idx - 1     # 다음 탐색
                continue
            idx -= 1

    codes = list(codes)
    for i in range(len(codes)):
        pw = []     # 암호 코드 숫자를 담을 리스트
        for j in range(0, 56, 7):
            pw.append(code[codes[i][j:j+7]])

        confirm = 0     # 올바른 암호코드인지 확인
        for j in range(8):
            if j % 2:
                confirm += pw[j]
            else:
                confirm += (pw[j] * 3)
        if confirm % 10 == 0:   # 올바른 암호코드일 경우
            result += sum(pw)

    print(f'#{tc}', result)
