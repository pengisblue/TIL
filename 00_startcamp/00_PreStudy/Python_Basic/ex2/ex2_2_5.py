def is_leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
N = int(input())
is_leap_year(N)
if is_leap_year(N): print(f'{N}년은 윤년입니다.')
else: print(f'{N}년은 윤년이 아닙니다.')