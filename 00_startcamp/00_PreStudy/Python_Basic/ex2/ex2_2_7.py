def Generation(year):
    if year <= 1924:
        return "The Greatest Generation"
    elif year <= 1945:
        return "The Silent Generation"
    elif year <= 1964:
        if year <= 1954 or year == 1964:
            ans = input('Are you Korean?(y/n) ')
            if ans == 'y':
                if year <= 1954:
                    return "The Silent Generation"
                else:
                    return "Generation X"
            else:
                return "baby boomer"
        else:
            return "baby boomer"
    elif year <= 1980:
        return "Generation X"
    elif year <= 1996:
        return "millennial"
    else: 
        return "Generation Z"

when = int(input('What year were you born? '))
print(Generation(when))