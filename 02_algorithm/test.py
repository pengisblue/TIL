s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'
print(s1, s2, s5)
if s1 == s5:
    print('s1 == s5')
else:
    print('s1 != s5')
if s1 is s5:
    print('s1 is s5')
else:
    print('s1 is not s5')