lst = ['1','2','3','4','5']

def test(a):
    for j in a:
        for i in j:
            if i in lst:
                return False, ['a','2']
            else: 
                return True

t = [['1','2','3'],['6','7','8']]

print(test(t))

